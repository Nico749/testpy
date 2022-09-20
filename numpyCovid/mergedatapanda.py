import matplotlib.pyplot as plt
from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')

import pandas as pd
covid_df = pd.read_csv('italy-covid-daywise.csv',encoding='utf-8-sig', sep='\s*,\s*', engine='python')

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')
# retrieve just the location from the new data
locations_df = pd.read_csv('locations.csv')
# print(locations_df[locations_df.location == "Italy"])

# We can merge this data into our existing data frame by adding more columns. However, to merge two data frames, we need at least one common column. 
# Let's insert a `location` column in the `covid_df` dataframe with all values set to `"Italy"`.NOTE
covid_df['location'] = "Italy"
# print(covid_df)
# We can now add the columns from locations_df into covid_df using the .merge method.
merged_df = covid_df.merge(locations_df, on="location")

# WE CAN CREATE CUSTOM MERGES TO ANALYSE DATA 
merged_df['newcases_per_million'] = merged_df.new_cases * 1e6 / merged_df.population
# print(merged_df)

# WRITE BACK THE RESULTS ON A CSV FILE
# result_df = merged_df[['date',
#                        'new_cases', 
#                        'total_cases', 
#                        'new_deaths', 
#                        'total_deaths', 
#                        'new_tests', 
#                        'total_tests', 
#                        'cases_per_million', 
#                        'deaths_per_million', 
#                        'tests_per_million']]

# result_df.to_csv('covid.csv', index=None)
