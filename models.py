from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    rating: float
    source: str
    link: str



    def to_dict(self):
        return{
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'source': self.source,
            'link': self.link
        }