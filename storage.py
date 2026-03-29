import csv 
import os
from models import Product
from exceptions import PriceTrackerError,FileOperationError,DataValidationError
from utils import timer

@timer
def save_products_to_csv(products, urunler):
    try:
        os.makedirs(os.path.dirname(urunler), exist_ok = True)
        file_exists = os.path.exists(urunler)
    except OSError as error:
        raise FileOperationError(f'Dosya Hatasi {error}')
    
    try:
        with open (urunler, mode='a', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames = ['name', 'price', 'rating', 'source', 'link'])
            if not file_exists :
                writer.writeheader()

            for urun in products:
                writer.writerow(urun.to_dict())
    except (OSError, csv.Error) as err:
        raise FileOperationError(f'Dosya hatasi {err}.')
    
@timer
def load_products_from_csv(urunler):

    try:
        nesne = []
        file_exists = os.path.exists(urunler)
        if file_exists:
            with open (urunler, mode='r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for prod in reader:
                    urun= Product(name = prod['name'], price= float(prod['price']), rating= float(prod['rating']), source= prod['source'], link= prod['link']) 
                    nesne.append(urun)       
        else:
                raise FileOperationError(f'Dosya bulunamadi.') 
         
    except (FileNotFoundError, OSError, csv.Error) as err:
        raise FileOperationError (f'Dosya hatasi {err}')

    return nesne



        
        
                

