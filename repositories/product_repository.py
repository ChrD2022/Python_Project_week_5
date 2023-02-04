from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (product_name, product_description, in_stock, buy_cost, sell_cost, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_description, product.in_stock, product.buy_cost, product.sell_cost, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(
            row['product_name'],
            row['product_description'],
            row['in_stock'],
            row['buy_cost'],
            row['sell_cost'],
            manufacturer
            )
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select[result['manufacturer_id']]
        product = Product(
            result['product_name'],
            result['product_description'],
            result['in_stock'],
            result['buy_cost'],
            result['sell_cost'],
            manufacturer
            )
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (product_name, product_description, in_stock, buy_cost, sell_cost, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.product_name, product.product_description, product.in_stock, product.buy_cost, product.sell_cost, product.manufacturer.id]
    run_sql(sql, values)
