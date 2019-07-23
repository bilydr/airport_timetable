# flask app
from flask import Flask, render_template, Markup
# from flask import request
import timetable

app = Flask(__name__)

@app.route('/')
def index():
    airports = ['MSP', 'CDG', 'SFO', 'DFW', 'SEA', 'BWI', "DLH"]
    return render_template('home.html', airports=airports)

@app.route('/departure/<airport>')
def departure(airport):
    time_table = Markup(timetable.get_time_table(airport, "departure"))
    return render_template('lookup.html', time_table=time_table, airport=airport, flight_type="departure")


@app.route('/arrival/<airport>')
def arrival(airport):
    time_table = Markup(timetable.get_time_table(airport, "arrival"))
    return render_template('lookup.html', time_table=time_table, airport=airport, flight_type="arrival")

@app.route('/about')
def info():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
