
from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify,flash
from ..ControllerExtensions.AdminAuthentication import AdminAuthentication
from ..models.category import *
from ..models.product import *
from ..models.trending import *
import sys,os,uuid
from pathlib import Path
from werkzeug.utils import secure_filename


class ProductController:
    @AdminAuthentication.check_auth
    def new(self,request,response,parameters):
        categories = Category.all().all()

        return render_template("/communications/admin/products_new.html",
                               categories=categories,dashboard_name="Products :New listing")
    @AdminAuthentication.check_auth
    def process_new(self,request,response,parameters):
        dir_name = str(uuid.uuid4())
        path = str(Path(os.getcwd())/"static/communications/uploaded/products/"/dir_name)

        try:
            os.mkdir(path)
        except:
            pass
        name = request.form["product_name"]
        desc = request.form["product_description"]
        price = request.form["product_price"]
        category_id = request.form["cat_parent"]
        new_prod = Product()
        new_prod.name = name
        new_prod.description = desc
        new_prod.category_id = category_id
        new_prod.price = price
        new_prod.image_directory = dir_name
        new_prod.save()
        return redirect('/communications/admin/products/view-all')

    @AdminAuthentication.check_auth
    def add_category(self, product):
        cat = Category.find(product.category_id)
        product.category_name = cat.name
        return product
    @AdminAuthentication.check_auth
    def view_all(self,request,response,parameters):
          products = [self.add_category(x) for x in Product.all().all()]
          return render_template("/communications/admin/product_view_all.html",
                               products=products,dashboard_name="Products :View All")
    @AdminAuthentication.check_auth
    def view(self,request,response,parameters):
        all_pos = [x for x in range(1,11)]
        curr_pos = [int(x.position) for x in Trending.all().all()]
        available= list(set(all_pos) - set(curr_pos))
        product = Product.find(parameters["product_id"])
        category = Category.find(product.category_id)
        product.category_name = category.name
        product.category_view = "/communications/admin/categories/view/"+str(category.id)
        path = str(Path(os.getcwd())/"static/communications/uploaded/products/"/str(product.image_directory))
        def _links(main,link):
            main = main.split("Web_Buy")[1]
            return main+"/"+link

        images = [_links(path,x) for x in os.listdir(path)]
        count = 1
        images2 = []
        for i in images:
            images2.append([count,i])
            count +=1


        return render_template("/communications/admin/product_view.html",
                               product=product,dashboard_name="Product :View",images=images2,positions=available)
    @AdminAuthentication.check_auth
    def upload_image(self,request,response,parameters):

        product = Product.find(parameters["product_id"])
        path = str(Path(os.getcwd())/"static/communications/uploaded/products/"/product.image_directory)
        if 'product_image' not in request.files:
            flash('No file part')
            return redirect("/communications/admin/products/view/"+parameters["product_id"])
        file = request.files['product_image']

        if file.filename == '':
            flash('No selected file')
            return redirect("/communications/admin/products/view/"+parameters["product_id"])
        filename = secure_filename(file.filename)
        print(os.path.join(path, filename))
        file.save(os.path.join(path, filename))
        return redirect("/communications/admin/products/view/"+parameters["product_id"])

    @AdminAuthentication.check_auth
    def trending(self,request,response,parameters):
        trending = Trending.all().all()
        all_trends = []
        for trend in trending:
            try:
                prod = Product.find_or_fail(trend.product_id)
                trend.name = prod.name
                trend.description = prod.description
                all_trends.append(trend)
            except:
                trend.delete()
                pass

        return render_template("/communications/admin/trending.html",dashboard_name="Trending",trends = all_trends)

    @AdminAuthentication.check_auth
    def trending_set(self,request,response,parameters):
        position = request.form["position"]
        product_id = position.split('-')[0]
        position = position.split('-')[1]

        if int(position) not in [x for x in range(1, 16)]:
            print(type(position))
            return jsonify({"message":"Unknown position"})
        try:
            prod = Product.find_or_fail(product_id)
        except:
            return jsonify({"message":"Product does not exist"})
        check_trend = Trending.where("position","=",position).first()
        if check_trend == None:
            trend = Trending()
            trend.product_id = product_id
            trend.position = position
            trend.save()
        else:
            check_trend.position = position
            check_trend.product_id = product_id
            check_trend.save()
        return redirect("/communications/admin/products/view/"+str(product_id))

    @AdminAuthentication.check_auth
    def trending_remove(self,request,response,parameters):
        trend_id = parameters["trend_id"]
        try:
            trend = Trending.find(trend_id)
            trend.delete()
        except:
            pass
        return redirect("/communications/admin/products/trending")