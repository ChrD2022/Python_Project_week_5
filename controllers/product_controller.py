from flask import Flask , render_template, request, redirect
from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product

from flask import Blueprint

product_blueprint = ("products", __name__)

