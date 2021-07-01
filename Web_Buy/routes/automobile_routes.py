from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
aut_routes = Blueprint('automobile_routes', __name__)