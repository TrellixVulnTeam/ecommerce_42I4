from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys


sys.path.append("../..")

from Utilities.communications.Loader import *
com_admin = Blueprint('communications_admin', __name__)
route_loader = Loader()


@com_admin.route("/login")
def login():
        return route_loader.load(controller="AdminController",action="login",request=request,response = {},parameters={})

@com_admin.route("/login-process",methods=["POST"])
def login_process():
        return route_loader.load(controller="AdminController",action="login_process",request=request,response = {},parameters={})

@com_admin.route("/dashboard")
def dashboard():
        return route_loader.load(controller="AdminController",action="dashboard",request=request,response={},parameters={})

@com_admin.route("/register")
def register():
        return route_loader.load(controller="AdminController",action="login",request=request,response = {},parameters={})

@com_admin.route("/register-process",methods=["POST"])
def register_process():
        return route_loader.load(controller="AdminController",action="login_process",request=request,response = {},parameters={})

@com_admin.route("/logout",)
def logout():
        return route_loader.load(controller="AdminController",action="logout",request=request,response = {},parameters={})

@com_admin.route("/categories/all",)
def category_view_all():
        return route_loader.load(controller="CategoryController",action="view_all",request=request,response = {},parameters={})


@com_admin.route("/categories/new",)
def category_new():
        return route_loader.load(controller="CategoryController",action="new",request=request,response = {},parameters={})

@com_admin.route('/categories/process-new',methods=['POST'])
def category_new_process():
        return route_loader.load(controller="CategoryController",action="process_new",request=request,response = {},parameters={})

@com_admin.route("/categories/view/<category_id>",)
def category_view(category_id):
        return route_loader.load(controller="CategoryController",action="view",request=request
                                 ,response = {},parameters={"category_id":category_id})

@com_admin.route("/categories/edit/<category_id>")
def category_edit(category_id):
        return route_loader.load(controller="CategoryController",action="edit",request=request
                                 ,response = {},parameters={"category_id":category_id})

@com_admin.route("/categories/update/<category_id>",methods=["POST"])
def category_update(category_id):
        return route_loader.load(controller="CategoryController",action="update",request=request
                                 ,response = {},parameters={"category_id":category_id})



@com_admin.route("/categories/delete/<category_id>")
def category_delete(category_id):
        return route_loader.load(controller="CategoryController",action="delete",request=request
                                 ,response = {},parameters={"category_id":category_id})

@com_admin.route("/products/new")
def products_new():
        return route_loader.load(controller="ProductController",action="new",request=request
                                 ,response = {},parameters={})
@com_admin.route("/products/process-new",methods=["POST"])
def products_process_new():
        return route_loader.load(controller="ProductController",action="process_new",request=request
                                 ,response = {},parameters={})
@com_admin.route("/products/view-all")
def products_view_all():
        return route_loader.load(controller="ProductController",action="view_all",request=request
                                 ,response = {},parameters={})
#/products/trending"

@com_admin.route("/products/view/<product_id>")
def products_view(product_id):
        return route_loader.load(controller="ProductController",action="view",request=request
                                 ,response = {},parameters={"product_id":product_id})

@com_admin.route("/products/image/<product_id>",methods=["POST"])
def products_image_upload(product_id):
        return route_loader.load(controller="ProductController",action="upload_image",request=request
                                 ,response = {},parameters={"product_id":product_id})



@com_admin.route("/products/trending")
def trendy_listing():
        return route_loader.load(controller="ProductController",action="trending",request=request
                                 ,response = {},parameters={})

@com_admin.route("/products/trending/",methods=["POST"])
def trending_set():
        return route_loader.load(controller="ProductController",action="trending_set",request=request
                                 ,response = {},parameters={})
#/communications/admin

@com_admin.route("/trend/delete/<trend_id>")
def trending_remove(trend_id):
        return route_loader.load(controller="ProductController",action="trending_remove",request=request
                                 ,response = {},parameters={"trend_id":trend_id})