from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys
sys.path.append("..")

from Utilities.communications.Loader import *
com_user = Blueprint('communications_user', __name__)
route_loader = Loader()

@com_user.route("/home/")
def home():
    return route_loader.load(controller="HomeController",action="home",request=request,response = {},parameters={})

@com_user.route("/home/view/<product_id>")
def home_view(product_id):
    return route_loader.load(controller="HomeController",action="view",request=request,response = {},parameters={"product_id":product_id})

@com_user.route("/get_started/")
def get_started():
    return route_loader.load(controller="HomeController", action="start", request=request, response={}, parameters={})

@com_user.route("/home/cart")
def cart():
    return route_loader.load(controller="HomeController",action="cart",request=request,response = {},parameters={})

#/communications/user/search
@com_user.route("/product/view/<product_id>")
def prod_view(product_id):
    return route_loader.load(controller="HomeController"
                             ,action="prod_view",request=request,
                             response = {},parameters={"product_id":product_id})

@com_user.route("search",methods=["POST"])
def search_prod():
    return route_loader.load(controller="HomeController"
                             ,action="search",request=request,
                             response = {},parameters={})

#/communications/user/cart/14/
@com_user.route("/cart/<product_id>/<user_id>")
def user_cart(product_id,user_id):
    return route_loader.load(controller="HomeController"
                             ,action="cart",request=request,
                             response = {},
                             parameters={"product_id":product_id,
                                         "user_id":user_id})

#/communications/user/cart/14/
@com_user.route("/cart/view")
def user_cart_view():
    return route_loader.load(controller="HomeController"
                             ,action="cart_view",request=request,
                             response = {},
                             parameters={})

@com_user.route('/cart/delete/<cart_id>')
def remove_from_cart(cart_id):
    return route_loader.load(controller="HomeController"
                             ,action="remove_from_cart",request=request,
                             response = {},
                             parameters={"cart_id":cart_id})
