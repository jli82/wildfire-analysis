import pandas as pd
import sqlite3

conn = sqlite3.connect('wildfire.sqlite')
wildfire_df = pd.read_sql_query('SELECT * FROM Fires', conn)
wildfire_df.to_csv('wildfire.csv', index=False)

weather_df = pd.read_csv('US_wildfire_weather_data.cvs')
weather_df.to_csv('weather.csv', index=False)