
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

    def view_all(self,request,response,parameters):
        categories = [self._get_parent(x) for x in Category.all().all()]
        return render_template("/communications/admin/category_view_all.html",dashboard_name="Category Dashboard",categories=categories)

    def new(self,request,response,parameters):

        categories = Category.all().all()
        return render_template("/communications/admin/category_new.html",dashboard_name="Category Dashboard: New",categories=categories)

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

