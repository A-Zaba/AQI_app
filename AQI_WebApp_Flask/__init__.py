from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='cop4814'

from AQI_WebApp_Flask import routes