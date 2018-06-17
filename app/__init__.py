from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', timestamp=time.time())


@app.route('/about')
def about():
    return render_template('about.html', timestamp=time.time())


@app.route('/training')
def training():
    return render_template('training.html', timestamp=time.time())


@app.route('/careers')
def careers():
    return render_template('careers.html', timestamp=time.time())


@app.route('/contact')
def contact():
    return render_template('contact.html', timestamp=time.time())

@app.route('/apply')
def apply():
    return render_template('job-form.html', timestamp=time.time())

@app.route('/test/personality')
def personality():
    return render_template('personality.html', timestamp=time.time())

if __name__ == '__main__':
    app.run(port=5000, debug=True)