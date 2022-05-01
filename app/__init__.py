from flask import Flask
from flask_bootstrap import Bootstrap

from config import DevConfig
app = Flask(__name__,instance_relative_config = True)
# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")
from app.main import views

# Initializing Flask Extensions
bootstrap = Bootstrap(app)