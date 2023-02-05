from flask import Flask , render_template, request, redirect
from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product
from models.manufacturer import Manufacturer

from flask import Blueprint

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

@product_blueprint.route("/products/<id>")
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product = product)

@product_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", all_manufacturers = manufacturers)

@product_blueprint.route("/products", methods=['POST'])
def create_new_product():
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    in_stock = request.form['in_stock']
    buy_cost = request.form['buy_cost']
    sell_cost = request.form['sell_cost']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(product_name, product_description, in_stock, buy_cost, sell_cost, manufacturer)
    product_repository.save(product)
    return redirect('/products')
