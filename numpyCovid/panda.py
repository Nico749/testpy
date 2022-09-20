# retrieve an url with the urlretrieve function 
from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')

import pandas as pd
# the read_csv is in
covid_df = pd.read_csv('italy-covid-daywise.csv')
# Data from the file is read and stored in a DataFrame object - one of the core data structures in Pandas for storing and working with tabular data. 
# We typically use the _df suffix in the variable names for dataframes.
# print(type(covid_df))
covid_df.info()
covid_df.columns
# TO SUMMARIZE
# pd.read_csv - Read data from a CSV file into a Pandas DataFrame object
# .info() - View basic infomation about rows, columns & data types
# .describe() - View statistical information about numeric columns
# .columns - Get the list of column names
# .shape - Get the number of rows & columns as a tuple

# retrieve a single value of the table
print(covid_df.at[246, 'new_cases'])
# extract a sample of the data 
print(covid_df.sample(10))

# covid_df['new_cases'] - Retrieving columns as a Series using the column name
# new_cases[243] - Retrieving values from a Series using an index
# covid_df.at[243, 'new_cases'] - Retrieving a single value from a data frame
# covid_df.copy() - Creating a deep copy of a data frame
# covid_df.loc[243] - Retrieving a row or range of rows of data from the data frame
# head, tail, and sample - Retrieving multiple rows of data from the data frame
# covid_df.new_tests.first_valid_index - Finding the first non-empty index in a series