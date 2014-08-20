from flask import render_template

from .. import app, mongo

@app.route('/')
def index():
  return render_template('index.html')
