# flask app
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./home.html')

@app.route('/info')
def info():
    return '<h1>About</h1>'

if __name__ == '__main__':
    app.run(debug=True)
