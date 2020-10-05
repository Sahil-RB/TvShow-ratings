from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hidden secret key to prevent csrf'
from app import routes
