from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
fin_routes = Blueprint('finance_routes', __name__)

