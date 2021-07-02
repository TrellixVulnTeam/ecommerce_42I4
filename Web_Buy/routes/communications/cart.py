from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys


sys.path.append("../..")

from Utilities.communications.Loader import *
com_cart = Blueprint('communications_cart', __name__)
route_loader = Loader()
