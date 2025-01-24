from flask import Flask
from flask_mysqldb import MySQL

class FlaskAppConfig:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.mysql = MySQL(self.app)

    def configure_app(self):
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = 'demo123'
        self.app.config['MYSQL_DB'] = 'movie_booking_system'
