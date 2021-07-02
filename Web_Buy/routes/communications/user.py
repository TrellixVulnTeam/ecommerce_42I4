from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys
sys.path.append("..")

from Utilities.communications.Loader import *
com_user = Blueprint('communications_user', __name__)
route_loader = Loader()

@com_user.route("/home/")
def home():
    return route_loader.load(controller="HomeController",action="home",request=request,response = {},parameters={})

# @com_routes.route("/communications/login/")
# def login():
#     return route_loader.load(controller="AuthController",action="login",request=request,response = {},parameters={})
#
# # @com_routes.route("/communications/login-process/")
# def process_login():
#     return route_loader.load(controller="AuthController",action="process_login",request=request,response = {},parameters={})
#
