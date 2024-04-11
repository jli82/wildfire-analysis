# import library
import pandas as pd
import sqlite3

# get wildfire data into dataframe
conn = sqlite3.connect('wildfire.sqlite')
wildfire_df = pd.read_sql_query('SELECT * FROM Fires', conn)
# get weather data into dataframe
weather_df = pd.read_csv('US_wildfire_weather_data.cvs')

# merge datasets
merged_df = wildfire_df.merge(weather_df, on='OBJECTID')
merged_df.columns = merged_df.columns.str.lower()

merged_df.to_csv('merged_df.csv', index=False)
