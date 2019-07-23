import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import config

# fetch timetable data from API and produce a html table
def get_time_table(airport, flight_type):
  api_url = 'http://airlabs.co/api/v7/timetable?api_key={0}&iata_code={1}&type={2}'.format(
      config.airlabs_key, airport, flight_type)
  req = requests.get(api_url)

  # response = json.loads(req.text) # dict
  response = req.json()['response']  # list
  df_res = json_normalize(response)

  # render dataframe as html
  html = df_res.to_html()
  return html
