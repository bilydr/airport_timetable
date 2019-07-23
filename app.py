# flask app
from flask import Flask, render_template
from flask import request
import timetable

app = Flask(__name__)

@app.route('/')
def index():
    airports = ['MSP', 'CDG', 'SFO', 'DFW', 'SEA', 'BWI', "DLH"]
    return render_template('home.html', airports=airports)

@app.route('/departure/<airport>')
def departure(airport):
    return timetable.get_time_table(airport, "departure")

@app.route('/arrival/<airport>')
def arrival(airport):
    return timetable.get_time_table(airport, "arrival")

@app.route('/about')
def info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
