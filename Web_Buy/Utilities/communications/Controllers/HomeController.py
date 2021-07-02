from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify

class HomeController:
    def home(self, request, response,parameters):

        return render_template("/communications/home.html",dashboard_name="IT & Communications")

