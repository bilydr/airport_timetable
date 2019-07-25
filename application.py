# flask application
from flask import Flask, render_template, Markup, session, redirect, url_for
# from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import timetable

application = Flask(__name__)
# config a secret key
application.config['SECRET_KEY'] = '1a2b3c5cdadf'


class InfoForm(FlaskForm):
    airport = StringField('Which airport (e.g. MSP)?',
                          validators=[DataRequired()])
    submit = SubmitField('Check Timetable')


@application.route('/', methods=['GET', 'POST'])
def index():

    airports = ['MSP', 'CDG', 'SFO', 'DFW', 'SEA', 'BWI', "DLH"]
    form = InfoForm()
    if form.validate_on_submit():
        my_airport = form.airport.data
        form.airport.data = ''
        return redirect(url_for('departure', airport=my_airport))

    return render_template('home.html', airports=airports, form=form)


@application.route('/departure/<airport>')
def departure(airport):
    time_table = Markup(timetable.get_time_table(airport, "departure"))
    return render_template('lookup.html', time_table=time_table, airport=airport, flight_type="departure")


@application.route('/arrival/<airport>')
def arrival(airport):
    time_table = Markup(timetable.get_time_table(airport, "arrival"))
    return render_template('lookup.html', time_table=time_table, airport=airport, flight_type="arrival")


@application.route('/about')
def info():
    return render_template('about.html')


if __name__ == '__main__':
    application.run(debug=True)
