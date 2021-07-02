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

