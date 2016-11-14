from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User
from app.models.subject import Subject

# create Blueprint class with name importname Blueprintfolders
classpage = Blueprint('classpage', __name__, url_prefix="/<url_user_id>/<url_Subject_id>/<url_Year>",
                      template_folder='', static_folder='')


@classpage.url_value_preprocessor
def class_process(endpoint, url_Subject_id):
    g.id = url_Subject_id['url_user_id']
    g.Subject_id = url_Subject_id['url_Subject_id']
    g.Year = url_Subject_id['url_Year']


@classpage.route('/')
def Subject(url_Subject_id, url_Year,url_user_id):
    return render_template('sub-1.html')


@classpage.route('/work')
def Subject_work(url_Subject_id, url_Year,url_user_id):
    g.subject=Subject(url_Subject_id,url_Year)
    return render_template('HTML_assignment.html')


@classpage.route('/Score')
def Subject_Score(url_Subject_id, url_Year,url_user_id):
    g.user = User(g.id)
    return 'boo'

@classpage.route('/<work_id>/score')
def Subject_work_score(url_Subject_id, url_Year,url_user_id,work_id):
    return 'boo'
