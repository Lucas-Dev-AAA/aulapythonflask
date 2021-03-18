from app import app


@app.rout('/')
@app.route('/index')
def index():
    return "Hello World"