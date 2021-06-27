from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
aut_routes = Blueprint('automotive_routes', __name__)