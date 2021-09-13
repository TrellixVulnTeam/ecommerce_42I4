

from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
from ..ControllerExtensions.AdminAuthentication import AdminAuthentication
from ..models.category import *
import sys
class CategoryController:
    def _get_parent(self,category):
            if category.parent_id == None:
                category.parent_name = "No Parent"
            else:
                parent =Category.find(category.parent_id)
                if parent == None:
                    category.parent_name = "No Parent"
                else:
                    category.parent_name = parent.name
            return category
    @AdminAuthentication.check_auth
    def view_all(self,request,response,parameters):
        categories = [self._get_parent(x) for x in Category.all().all()]
        return render_template("/communications/admin/category_view_all.html",dashboard_name="Category Dashboard",categories=categories)
    @AdminAuthentication.check_auth
    def new(self,request,response,parameters):

        categories = Category.all().all()
        return render_template("/communications/admin/category_new.html",dashboard_name="Category Dashboard: New",categories=categories)
    @AdminAuthentication.check_auth
    def process_new(self,request,response,parameters):
        if request.method == "POST":
            cat_name = request.form["cat_name"]
            cat_desc = request.form["cat_desc"]
            new_cat = Category()
            new_cat.name = cat_name
            new_cat.description = cat_desc
            if "cat_parent" in request.form.keys():
                new_cat.parent_id = request.form["cat_parent"]
            new_cat.save()

        return redirect("/communications/admin/categories/all")

    @AdminAuthentication.check_auth
    def view(self,request,response,parameters):
        category = Category.find(parameters['category_id'])
        parent = Category.find(category.parent_id)
        if parent == None:
            category.parent_name = "No Parent"
            category.parent_view = "#"
        else:
            category.parent_name = parent.name
            category.parent_view = "/communications/admin/categories/view/"+str(parent.id)
        return render_template("/communications/admin/category_view.html",dashboard_name="Category Dashboard: View",category=category)

    @AdminAuthentication.check_auth
    def edit(self,request,response,parameters):
        category = Category.find(parameters["category_id"])
        categories = Category.all().all()
        return render_template("/communications/admin/category_edit.html",
                               dashboard_name="Category Dashboard: Edit",
                               category=category,categories=categories)

    @AdminAuthentication.check_auth
    def update(self,request,response,parameters):
        if request.method == "POST":
            cat_name = request.form["cat_name"]
            cat_desc = request.form["cat_desc"]
            new_cat = Category.find(parameters["category_id"])
            new_cat.name = cat_name
            new_cat.description = cat_desc
            if "cat_parent" in request.form.keys():
                new_cat.parent_id = request.form["cat_parent"]
            new_cat.save()
        return redirect("/communications/admin/categories/all")

    @AdminAuthentication.check_auth
    def delete(self,request,response,parameters):
        try:
            category = Category.find(parameters["category_id"])
            category.delete()
        except:
            pass
        return redirect("/communications/admin/categories/all")
