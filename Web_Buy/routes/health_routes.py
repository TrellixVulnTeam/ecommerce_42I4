from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
hea_routes = Blueprint('health_routes', __name__)