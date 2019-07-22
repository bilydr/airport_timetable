# flask app
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    airport = "MSP"
    return render_template('./home.html', airport=airport)


@app.route('/info')
def info():
    return '<h1>About</h1>'


if __name__ == '__main__':
    app.run(debug=True)
