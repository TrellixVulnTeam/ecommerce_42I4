from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
fas_routes = Blueprint('fashion_routes', __name__)