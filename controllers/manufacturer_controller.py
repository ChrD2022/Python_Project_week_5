from flask import Flask , render_template, request, redirect
from repositories import manufacturer_repository
from repositories import product_repository
from models.manufacturer import Manufacturer

from flask import Blueprint

manufacturer_blueprint = Blueprint("manufacturers", __name__)

@manufacturer_blueprint.route