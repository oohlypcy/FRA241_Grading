from flask import Flask,redirect,url_for
from login.views import Login
from homepage.views import Homepage
from classpage.views import classpage
from score.views import score
from addpage.views import Addpage
#declare flask app
Grading = Flask(__name__)
#register blueprint
Grading.register_blueprint(Login)
Grading.register_blueprint(Homepage)
Grading.register_blueprint(classpage)
Grading.register_blueprint(Addpage)
#default route
@Grading.route('/')
def default():
    return redirect(url_for('login.login'))

#run app
Grading.run()