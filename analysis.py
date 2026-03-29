import numpy as np
import pandas as pd
from models import Product
from utils import timer

@timer
def analyze_products(products):
    data= [uruns.to_dict()  for uruns in products]  
    df= pd.DataFrame(data)
    if df.empty:
        return None
    
    df['price']= pd.to_numeric(df['price'], errors= 'coerce')
    price_array= df['price'].dropna().to_numpy()
    df['rating']= pd.to_numeric(df['rating'], errors= 'coerce')

    stats={
        'urun_sayisi': len(price_array),
        'ortalama_fiyat': np.mean(price_array),
        'max_fiyat': np.max(price_array),
        'min_fiyat': np.min(price_array),
        'medyan_fiyat': np.median(price_array)
    }

    grouped= df.groupby('rating')['price'].mean().reset_index()
    grouped.columns= ['rating', 'ortalama_fiyat']

    return stats,grouped



@timer
def get_top_expensive_products(products, top_n=5):
    data= [uruns.to_dict() for uruns in products ]
    df= pd.DataFrame(data)
    


    if df.empty:
        return None
    else:
        df['price']= pd.to_numeric(df['price'], errors= 'coerce' )
        sorted_df= df.sort_values('price', ascending= False).head(top_n)

    return sorted_df
