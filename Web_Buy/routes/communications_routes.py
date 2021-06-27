from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
com_routes = Blueprint('communications_routes', __name__)

@com_routes.route("/communications/example")
def exmple():
    return render_template("communications/example.html")

