import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = time.time()
        result = func(*args, **kwargs)
        afternow = time.time()
        sonuc = afternow - now
        print(f' {func.__name__} fonksiyonu {sonuc: .4f} saniye sürdü')


        return result
    return wrapper


def apply_operation(data, operation):
    return [operation(item) for item in data]



def create_price_filter(min_price):
    def price_check(product):
        return product.price >= min_price
    return price_check



