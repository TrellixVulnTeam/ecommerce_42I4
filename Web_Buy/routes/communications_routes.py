from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys

# from Web_Buy.Utilities.communications.Loader import Loader

sys.path.append("..")

# import ..Utili
from Utilities.communications.Loader import *
com_routes = Blueprint('communications_routes', __name__)
route_loader = Loader()

@com_routes.route("/communications/home/")
def home():
    return route_loader.load(controller="HomeController",action="home",request=request,response = {},parameters={})

@com_routes.route("/communications/login/")
def login():
    return route_loader.load(controller="AuthController",action="login",request=request,response = {},parameters={})

@com_routes.route("/communications/login-process/")
def login():
    return route_loader.load(controller="AuthController",action="process_login",request=request,response = {},parameters={})

