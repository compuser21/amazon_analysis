from scraper import *
from excel import *

def main():
    print('-' * 50)
    print('Amazon Competitors Products Info')
    print('-' * 50)
    
    #1. Scraping ASIN list (target is 500 products)
    keyword = 'laptop'
    
    print(f"Searching '{keyword}'...")
    asins = get_asins_from_search(keyword, max_pages=32) #32 pages * 16 ≈ 512 products
    
    print(f'preparing to get {len(asins)} products details, it will take some time...')
    
    #2. Batching data
    products = get_products_batch(asins, delay=2)
    
    #3. Saving to Excel table
    save_to_excel(products)
    
    #4. Showing statistics
    print("\n" + "=" * 50)
    print('Product statistics:')
    print(f'Total count: {len(products)}')
    
    # Calculating average price
    prices = []
    for p in products:
        try:
            price_clean = p['price'].replace('AZN', '').replace(',', '')
            prices.append(float(price_clean))
        except:
            pass
        
    if prices:
        avg_prices = sum(prices) / len(prices)
        print(f'Average price: AZN{avg_prices:.2f}')
        
    print('-' * 50)
    
#Running
if __name__ == '__main__':
    main()
        
    
    