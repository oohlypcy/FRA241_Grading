from flask import Flask, Blueprint, render_template, g, request, json, jsonify, url_for
import sqlite3
from app.models.user import User
from app.models.subject import Subject
from app.models.submitWork import submitWork
from app.models.work import Work
import datetime
# create Blueprint class with name importname Blueprintfolders
Addpage= Blueprint('Addpage', __name__, url_prefix="/<url_user_id>", template_folder='', static_folder='')

@Addpage.route('/<url_Subject_id>/<url_Year>/add_work')
def add_assignment(url_user_id,url_Subject_id,url_Year):
    return 'boo'

@Addpage.route('/add_subject')
def add_subject(url_user_id):
    return 'boo'

@Addpage.route('/<url_Subject_id>/<url_Year>/add_student')
def add_student(url_user_id,url_Subject_id,url_Year):
    return 'boo'

@Addpage.route('/<url_Subject_id>/<url_Year>/<work_id>/manage_group')
def manage_group(url_user_id,url_Subject_id,url_Year,work_id):
    return 'boo'
