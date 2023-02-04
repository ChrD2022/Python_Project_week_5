from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers (manufacturer_name, manufacturer_location) VALUES (%s, %s) RETURNING *"
    values = [
        manufacturer.manufacturer_name,
        manufacturer.manufacturer_location
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * From manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(
            row['manufacturer_name'],
            row['manufacturer_location'],
            row['id']
            )
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT* FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        manufacturer = Manufacturer(
            result['manufacturer_name'],
            result['manufacturer_location'],
            result['id']
            )
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete_id(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (manufacturer_name, manufacturer_location) = (%s, %s) WHERE id = %s"
    values = [
        manufacturer.manufacturer_name,
        manufacturer.manufacturer_location,
        manufacturer.id
        ]
    run_sql(sql, values)

def products(manufacturer):
    products = []

    sql = "SELECT * FROM products Where manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(
            row['product_name'],
            row['product_description'],
            row['in_stock'],
            row['buy_cost'],
            row['sell_cost'],
            row['manufacturer_id'],
            row['id']
            )

