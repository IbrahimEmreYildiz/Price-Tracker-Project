from scraper import scrape_products, ProductIterator, product_generator
from storage import save_products_to_csv, load_products_from_csv
from analysis import analyze_products, get_top_expensive_products
from utils import apply_operation, create_price_filter
from exceptions import WebScrapingError, FileOperationError

def main():
    url= 'https://books.toscrape.com/catalogue/page-1.html'
    filename= 'data/products.csv'

    try:
        print("1) Veriler web'den çekiliyor...")
        scraped_products=scrape_products(url)

        print(f"Toplam çekilen ürün sayisi:{len(scraped_products)}")

        print("\n2) Iterator ile ilk 3 urun gosteriliyor..")

        iterator= ProductIterator(scraped_products)
        count=0
        for product in iterator:
            print(f"-{product.name} | £{product.price} | Rating:{product.rating}")
            count+= 1
            if count ==3:
                break

        print("\n3) Generator ile ilk 3 ürünü gösterelim:")

        gen=product_generator(scraped_products)
        for _ in range(3):
            product= next(gen)
            print(f"-{product.name}")

        print("\n4) Veriler CSV'ye kaydediliyor..")
        save_products_to_csv(scraped_products, filename)
        
        print("\n5) CSV'den tekrar okunuyor..")
        loaded_products= load_products_from_csv(filename)

        print(f'Okunan kayit sayisi {len(loaded_products)}')

        print("\n6) Seçtiğiniz miktardan pahali urunler listesi çikariliyor..")
        sinir= int(input("Sinir kaç Euro olsun: "))
        price_filter= create_price_filter(sinir)
        filtered_products= list(filter(price_filter, loaded_products))
        print(f"{sinir} ve üzeri ürün sayisi:{len(filtered_products)}")

        print("\n7) Veri analizi yapiliyor...")
        stats,grouped= analyze_products(loaded_products)

        if stats:
            print("\nGenel İstatistikler:")
            for key,value in stats.items():
                print(f"{key}:{value}")

        print("\nRating'e göre ortalama fiyat:")
        print(grouped)

        print("\n8) En pahali 5 ürün:")
        top_products= get_top_expensive_products(loaded_products, top_n=5)
        print(top_products[["name","price","rating"]])
    except WebScrapingError as e:
        print(f"[SCRAPING HATASI]{e}")
    except FileOperationError as e:
        print(f"[DOSYA HATASI]{e}")
    except Exception as e:
        print(f"[GENEL HATA]{e}")


if __name__== "__main__":
    main()
