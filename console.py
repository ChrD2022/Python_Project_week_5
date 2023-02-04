import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Incom Corp.", "Fresia")
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Sienar Fleet sys.", "Lianna")
manufacturer_repository.save(manufacturer_2)

product_1 = Product("X-Wing", "The perfect starfighter for your rebelling needs.",
50, 150000, 175000, manufacturer_1)
product_repository.save(product_1)
product_2 = Product("TIE Fighter", "An Imperial classic.", 100, 60000, 80000, manufacturer_2)
product_repository.save(product_2)
product_3 = Product("TIE Interceptor", "The Imperial gentleman's choice.", 60, 75000, 90000, manufacturer_2)
product_repository.save(product_3)


pdb.set_trace()