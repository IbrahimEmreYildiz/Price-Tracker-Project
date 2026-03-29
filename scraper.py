import requests
from bs4 import BeautifulSoup

from models import Product
from exceptions import WebScrapingError
from utils import timer


class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        item = self.products[self.index]
        self.index += 1
        return item


def product_generator(products):
    for product in products:
        yield product


@timer
def scrape_products(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise WebScrapingError(f"Web sayfası alınamadı: {e}")

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        product_cards = soup.select("article.product_pod")
        products = []

        for card in product_cards:
            name = card.h3.a["title"].strip()

            price_text = card.select_one(".price_color").text.strip()
            price = float(price_text.replace("£", "").replace("Â", ""))

            rating_class = card.select_one("p.star-rating")["class"]
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = 0
            for cls in rating_class:
                if cls in rating_map:
                    rating = rating_map[cls]
                    break

            relative_link = card.h3.a["href"]
            full_link = "https://books.toscrape.com/catalogue/" + relative_link.replace("../../../", "")

            product = Product(
                name=name,
                price=price,
                rating=rating,
                source="books.toscrape.com",
                link=full_link
            )
            products.append(product)

        return products

    except Exception as e:
        raise WebScrapingError(f"Sayfa parse edilirken hata oluştu: {e}")