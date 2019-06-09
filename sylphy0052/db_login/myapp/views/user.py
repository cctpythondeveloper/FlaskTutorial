"""
Program for View control user data
"""

from flask import request, redirect, url_for, render_template, flash, session
from myapp import app
from myapp.views.view import login_required
from flask import Blueprint
from myapp.controller.dbcontroller import search_user_by_id

user = Blueprint('user', __name__)

@user.route('/<int:userid>')
@login_required
def show_toppage(userid):
    user = search_user_by_id(userid)
    return render_template('user/toppage.html', user=user)
