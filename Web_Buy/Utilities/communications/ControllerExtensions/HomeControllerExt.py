
from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
from ..models.product import *
from ..models.trending import *
from ..models.category import *
from ..models.cart import *
import sys,os
from pathlib import Path
from datetime import datetime

class HomeControllerExt:

    def prod_view(self,request,response,parameters):
        product = Product.find(parameters["product_id"])
        category = Category.find(product.category_id)
        product.category_name = category.name
        product.category_view = "/communications/admin/categories/view/" + str(category.id)
        path = str(Path(os.getcwd()) / "static/communications/uploaded/products/" / str(product.image_directory))

        def _links(main, link):
            main = main.split("Web_Buy")[1]
            return main + "/" + link

        images = [_links(path, x) for x in os.listdir(path)]
        count = 1
        images2 = []
        for i in images:
            images2.append([count, i])
            count += 1
        search_cats = Category.all().all()
        return render_template("/communications/front/product_view.html",
                               product=product, page_heading="Product :View", images=images2,
                               categories = search_cats)

    def cart(self,request,response,parameters):
        product_id = parameters["product_id"]
        user_id = parameters["user_id"]
        cart = Cart()
        cart.user_id = user_id
        cart.count = 1
        cart.timestamp_reserved =datetime.now()
        cart.product_id = product_id
        cart.save()
        return redirect("/communications/user/product/view/"+str(product_id))

    def cart_view(self,request,response,parameters):
        def _load_product(cart_item):
            product = Product.find(cart_item.product_id)
            product.cart_item_id = cart_item.id
            product.count = cart_item.count
            print("****************")
            print(product)
            print("****************")
            return product

        cart_items = [_load_product(cart_item) for cart_item in  Cart.all().all()]
        print("****************")
        print(Cart.all().all())
        print("****************"*80)
        return render_template("/communications/front/cart_view.html",
                               page_heading="Cart :View",
                               carts=cart_items)

    def remove_from_cart(self,request,response,parameters):
        cart_id = parameters["cart_id"]
        try:
            cart_item = Cart.find(cart_id)
            cart_item.delete()
        except:
            pass
        return redirect('/communications/user/cart/view')

