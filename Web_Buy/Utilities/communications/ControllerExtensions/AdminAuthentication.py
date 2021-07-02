from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys
from ..models.admin import *

class AdminAuthentication:
    def login(self, request, response,parameters):
        message = request.args.get('message')
        if message == None:
            return render_template("/communications/admin/login.html")
        else:
            return render_template("/communications/admin/login.html",error_message=message)

    def login_process(self, request, response,parameters):
        if request.method == 'POST':
            email = request.form["email_address"]
            password = request.form["password"]
            admin = Admin.where("email","=",email).where("password","=",password).first()
            if admin == None:
                message = "Login failed please check email or password and retry"
                return redirect("/communications/admin/login?message='"+message+"'")
            session["admin_id"] = admin.id
            session["admin_first_name"] = admin.first_name
            session["admin_last_name"] = admin.last_name
            session["admin_email"] = admin.email
            session["admin_profile_pic"] = admin.profile_pic
            return redirect("/communications/admin/dashboard")

    def logout(self,request,response,parameters):
        try:
            session.pop('admin_id')
        except:
            pass
        try:
            session.pop('admin_first_name')
        except:
            pass
        try:
            session.pop('admin_last_name')
        except:
            pass
        try:
            session.pop('admin_email')
        except:
            pass
        try:
            session.pop('admin_profile_pic')
        except:
            pass

        return redirect("/communications/admin/login")
    @staticmethod
    def check_auth(func):
        def wrapper(*args, **kwargs):
            if 'admin_id' not in session:
                message="You need to login first to access any part of the admin dashboard"
                return redirect("/communications/admin/login?message='"+message+"'")
            return func(*args, **kwargs)
        return wrapper


