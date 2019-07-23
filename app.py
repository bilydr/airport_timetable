# flask app
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    airports = ['MSP', 'CDG', 'SFO', 'DFW', 'SEA', 'BWI']
    return render_template('home.html', airports=airports)

@app.route('/lookup')
def lookup():
    return "<h3>Your airport's timetable will appear here</h3>"

@app.route('/top')
def top_airport():
    return "<h3>top airports will appear here</h3>"


@app.route('/about')
def info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
