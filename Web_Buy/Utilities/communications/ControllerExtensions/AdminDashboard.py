from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
from .AdminAuthentication import *
class AdminDashboard:
    @AdminAuthentication.check_auth
    def dashboard(self,request,response,parameters):
        return render_template("/communications/admin/home.html",dashboard_name="Admin dashboard")
