from .. import app, mongo

@app.route('/')
def index():
  return 'Hello list!'
