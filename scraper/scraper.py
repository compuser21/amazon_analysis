import requests
from bs4 import BeautifulSoup
import time
import re
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
]

headers = {
    'User-Agent': random.choice(user_agents),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def get_asins_from_search(keyword, max_pages=20):
    '''
    Using product's ASIN to find all goods of some type in Amazon
    keywords: searching keyword, example: laptop
    max_pages: biggest number of pages to scrape from (each page has 16 goods)
    '''
    
    all_asins = []
    
    for page in range(1, max_pages + 1):
        url = f'https://www.amazon.co.uk/s?k={keyword}&page={page}&rh=n%3A172282%2Cp_72%3A1248879011'
        print(f"searching {page} page...")
        
        try: 
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            items = soup.select('div[data-asin]')
            page_asins = []
            
            for item in items:
                asin = item.get('data-asin')
                if asin and asin != '':
                    page_asins.append(asin)
                    all_asins.append(asin)
                    
            print(f'page {page} has {len(page_asins)} goods')
        
            #If there is no any goods left
            if len(page_asins) == 0:
                print('No goods left, stopping scraping')
                break
            
            #If 500 goods already have been scraped
            if len(all_asins) >= 500: 
                print(f"there are already {len(all_asins)} goods, that's enough")
                break
            
            #after scraping each page sleeping for 3 seconds
            time.sleep(3)
        
        except Exception as e:
            print(f'during scraping page {page}, error {e} occured')
            break
        
    #if there are more than 500 goods, take first 500 only
    if len(all_asins) > 500: 
        all_asins = all_asins[:500]  
        
    print(f'\ntotally {len(all_asins)} ASINs scraped')
    return all_asins

#getting info of product
def get_product_info(asin):
    '''getting detailed information about product'''
    url = f'https://www.amazon.com/dp/{asin}'
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_tag = soup.select_one('#productTitle')
        title = title_tag.text.strip() if title_tag else 'UNKNOWN'
        
        price_tag = soup.select_one('span.a-price .a-offscreen')
        price = price_tag.text.strip() if price_tag else 'UNKNOWN'
        
        rating_tag = soup.select_one('#acrPopover')
        rating = rating_tag.get('title', '') if rating_tag else ''
        rating_match = re.search(r'(\d+\.?\d*)', rating)
        rating = rating_match.group(1) if rating_match else 'UNKNOWN'
        
        review_tag = soup.select_one('#acrCustomerReviewText')
        review_count = review_tag.text.strip() if review_tag else 'UNKNOWN'
        review_match = re.search(r'(\d+)', review_count)
        reviews = review_match.group(1) if review_match else '0'
        
        brand_tag = soup.select_one('#bylineInfo')
        brand = brand_tag.text.strip() if brand_tag else 'UNKNOWN'
        # deleting prefix like 'Visit the'
        brand = re.sub(r'^Visit the | Store$', '', brand).strip()
        
        if (title != 'UNKNOWN' and
            brand != 'UNKNOWN' and
            price != 'UNKNOWN' and
            rating != 'UNKNOWN' and
            reviews != 'UNKNOWN'):
            return {
                'asin': asin,
                'title': title,
                'brand': brand,
                'price': price,
                'rating': rating,
                'reviews': reviews
            }
        else: return None
        
    except Exception as e:
        print(f'in asin {asin}, error {e} occured')
        return None
    
def get_products_batch(asins, delay=2):
    '''
    Batching product info
    asins: lists of ASIN
    delay: number of seconds between each request
    '''
    products = []
    total = len(asins)
    
    for i, asin in enumerate(asins):
        print(f'getting [{i+1}/{total}]: {asin}')
        product = get_product_info(asin)
        
        if product:
            products.append(product)
            print(f"  ✓ {product['title'][:40]}...")
        else:
            print(f"  ✗ error during batching")
            
        #sleeping after every 10 products
        if (i + 1) % 10 == 0:
            print(f"  already got {i+1} products, sleeping for 5 seconds...")
            time.sleep(5)
        else:
            time.sleep(delay)
            
    print(f'\nsuccessfully getting info of {len(products)} products')
    return products
    
    