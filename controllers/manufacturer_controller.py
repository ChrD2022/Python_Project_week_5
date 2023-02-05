from flask import Flask , render_template, request, redirect
from repositories import manufacturer_repository
from repositories import product_repository
from models.manufacturer import Manufacturer

from flask import Blueprint

manufacturer_blueprint = Blueprint("manufacturers", __name__)

@manufacturer_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

@manufacturer_blueprint.route("/manufacturers/<id>")
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer=manufacturer)

@manufacturer_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/new.html", manufacturers = manufacturers)

@manufacturer_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    manufacturer_name = request.form['manufacturer_name']
    manufacturer_location = request.form['manufacturer_location']
    manufacturer = Manufacturer(manufacturer_name, manufacturer_location)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturer_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

@manufacturer_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('/manufacturers/edit.html', manufacturer = manufacturer)

@manufacturer_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    manufacturer_name = request.form['manufacturer_name']
    manufacturer_location = request.form['manufacturer_location']
    manufacturer = Manufacturer(manufacturer_name, manufacturer_location, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')
