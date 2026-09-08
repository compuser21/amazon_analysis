from openpyxl import Workbook

def save_to_excel(products, filename='amazon_products.xlsx'):
    '''saving product info to Excel table'''
    wb = Workbook()
    ws = wb.active
    ws.title = 'Product info'
    
    #adding tables
    headers = ['Serial number', 'ASIN', 'Title', 'Brand', 'Price', 'Rating', 'Reviews']
    ws.append(headers)
    
    #filling data
    for i, p in enumerate(products, 1):
        ws.append([
            i,
            p['asin'],
            p['title'],
            p['brand'],
            p['price'],
            p['rating'],
            p['reviews']
        ])
        
    #Adjusting column width (to make table looking better)
    column_widths = [8, 15, 60, 20, 15, 12, 15]
    for col, width in enumerate(column_widths, 1):
        ws.column_dimensions[chr(64 + col)].width = width
        
    #saving in file
    wb.save(filename)
    print(f'\ndata saved in {filename}')