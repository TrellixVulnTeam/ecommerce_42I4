from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
from ..models.product import *
from ..models.trending import *
import sys,os
from ..ControllerExtensions.HomeControllerExt import *
from pathlib import Path
class HomeController(HomeControllerExt):
    def home(self, request, response,parameters):
        _all = ["position_" + str(x) for x in range(1, 16)]
        trending = Trending.all().all()
        products = {}
        # trending = Product.all().all()
        print(trending)
        # sys.exit()
        for trend in trending:
            try:
                prod = Product.find_or_fail(trend.product_id)
                trend.name = prod.name

                trend.description = prod.description
                img_dir = "/static/communications/uploaded/products/"
                img_dir = img_dir + prod.image_directory
                tmp = os.getcwd()+img_dir
                print(tmp)
                dir_content = os.listdir(tmp)
                print(dir_content)
                if len(dir_content) < 0:
                    first_image = ""
                else:
                    first_image = dir_content[0]
                image = img_dir + "/" + first_image
                print(dir_content)
                trend.image = image
                products["position_"+str(trend.position)] = trend
            except Exception  as e:
                print(e)
                trend.delete()
                pass


        diff = list(set(_all) - set(products.keys()))
        dummy = Trending()
        dummy.name = "Not Set"
        dummy.image = "https://image.shutterstock.com/image-vector/ui-image-placeholder-wireframes-apps-260nw-1037719204.jpg"
        for pos in diff:
            products[pos] = dummy
        search_cats = Category.all().all()
        return render_template("/communications/front/home.html",
                               dashboard_name="IT & Communications",products=products
                               ,page_heading="Trending Products",categories=search_cats)

    def search(self, request, response,parameters):
        category_q= request.form["category"]
        product_q = str(request.form["product_name"])
        product_builder = Product.where('name','=',product_q)
        all = None
        if category_q != '1234':
            product_builder = product_builder.where('category_id','=',category_q)

        return jsonify({})


    def view(self, request, response, parameters):
        products = Product.find(parameters['product_id'])
        return render_template("/communications/shop-single.html", dashboard_name= "Product Details",
                               products=products)

    def start(self, request, response, parameters):
        return render_template("/communications/front/get_started.html", dashboard_name= "Get Started")


    #def user_cart(self, request=POST):

