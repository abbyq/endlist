import logging
import os
import urllib

import flask
from flask.ext.pymongo import PyMongo

from . import config

app = flask.Flask(__name__)
if os.environ.get('SCRIPTSLASH_MODE') == 'production':
  app.config.from_object(config.ProductionConfig)
else:
  app.config.from_object(config.DevelopmentConfig)

mongo = PyMongo(app)

import views
