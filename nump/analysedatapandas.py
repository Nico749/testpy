from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')

import pandas as pd
covid_df = pd.read_csv('italy-covid-daywise.csv',encoding='utf-8-sig', sep='\s*,\s*', engine='python')

# even in pandas as in numpy we can do operations with data 
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))

death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))

# we can also apply conditions 
high_cases_df = covid_df[covid_df.new_cases > 1000]
# print(high_cases_df)

# The rows can also be sorted by a specific column using .sort_values. Let's sort to identify the days with the highest number of cases, 
# then chain it with the head method to list just the first ten results.
print(covid_df.sort_values('new_cases', ascending=False).head(10))

# WHAT IF WE HAVE DATA ERRORS LIKE IN THIS SUBSET?
# we can either:
# Replace it with 0.
# Replace it with the average of the entire column
# Replace it with the average of the values on the previous & next date
# Discard the row entirely
print(covid_df.sort_values('new_cases').head(10))
# we replace that data with the average of the days close to that 
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2
# print(covid_df.sort_values('new_cases').head(10))

# TO SUMMARIZE
# covid_df.new_cases.sum() - Computing the sum of values in a column or series
# covid_df[covid_df.new_cases > 1000] - Querying a subset of rows satisfying the chosen criteria using boolean expressions
# df['pos_rate'] = df.new_cases/df.new_tests - Adding new columns by combining data from existing columns
# covid_df.drop('positive_rate') - Removing one or more columns from the data frame
# sort_values - Sorting the rows of a data frame using column values
# covid_df.at[172, 'new_cases'] = ... - Replacing a value within the data frame

# WE CAN ALSO GROUPBY VALUES 
# covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
