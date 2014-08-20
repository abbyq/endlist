import os

class Config(object):
  DEBUG = False
  TESTING = False
  MONGO_URI = 'mongodb://localhost:27017/list_dev'

class ProductionConfig(Config):
  MONGO_URI = os.environ.get('MONGOLAB_URI')

class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
