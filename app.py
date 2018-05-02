from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'homepage'


@app.route('/about')
def about():
    return 'aboutpage'


@app.route('/projects')
def projects():
    return 'projectpage'


@app.route('/careers')
def careers():
    return 'carrerspage'


@app.route('/contact')
def contact():
    return 'contactpage'


app.run(port=5000, debug=True)