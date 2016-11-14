import sqlite3
from flask import url_for
from flask import request
# declare class
class file:
    def upload_file(self):
        if request.method == 'POST':
            f = request.files['the_file']
            f.save('/var/www/uploads/uploaded_file.pdf')
