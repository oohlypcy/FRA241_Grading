from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User

# create Blueprint class with name importname Blueprintfolders
classpage = Blueprint('classpage', __name__, url_prefix="/<url_Subject_id>", template_folder='', static_folder='')


@classpage.url_value_preprocessor
def class_process(url_Subject_id):
    pass


@classpage.route('/')
def Subject(url_Subject_id):
    return 'boo'


@classpage.route('/work')
def Subject_work(url_Subject_id):
    return 'boo'


@classpage.route('/Score')
def Subject_Score(url_Subject_id):
    return 'boo'
