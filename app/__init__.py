from flask import Flask,redirect,url_for
from login.views import Login
from homepage.views import Homepage
#declare flask app
Grading = Flask(__name__)
#register blueprint
Grading.register_blueprint(Login)
Grading.register_blueprint(Homepage)
#default route
@Grading.route('/')
def default():
    return redirect(url_for('login.login'))

#run app
Grading.run()