# importing dataset from kaggle
import opendatasets as od
od.download('stackoverflow-developer-survey-2020')
import os
os.listdir('stackoverflow-developer-survey-2020')

import pandas as pd
survey_raw_df = pd.read_csv('stackoverflow-developer-survey-2020/survey_results_public.csv')
# print(survey_raw_df.columns) gives back the columns of the db

# We can refer to the schema file to see the full text of each question
schema_fname = 'stackoverflow-developer-survey-2020/survey_results_schema.csv'
schema_raw = pd.read_csv(schema_fname, index_col='Column').QuestionText
# print(schema_raw)

# DATA PREPARATION, we pick only the column we need
selected_columns = [
    # Demographics
    'Country',
    'Age',
    'Gender',
    'EdLevel',
    'UndergradMajor',
    # Programming experience
    'Hobbyist',
    'Age1stCode',
    'YearsCode',
    'YearsCodePro',
    'LanguageWorkedWith',
    'LanguageDesireNextYear',
    'NEWLearn',
    'NEWStuck',
    # Employment
    'Employment',
    'DevType',
    'WorkWeekHrs',
    'JobSat',
    'JobFactors',
    'NEWOvertime',
    'NEWEdImpt'
]
# make a copy so we can modify without altering the original data
survey_df = survey_raw_df[selected_columns].copy()
schema = schema_raw[selected_columns]
# survey_df.info() #get some basic info 
# convert these columns values into numbers to make the analysis easier, the other values are evaluated as NaN
survey_df['Age1stCode'] = pd.to_numeric(survey_df.Age1stCode, errors='coerce')
survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')
# with describe we can see if our data is cleaned or biased
# print(survey_df.describe())

# since we have problems with age and workweekhrs, we drop outliers 
survey_df.drop(survey_df[survey_df.Age < 10].index, inplace=True)
survey_df.drop(survey_df[survey_df.Age > 100].index, inplace=True)
survey_df.drop(survey_df[survey_df.WorkWeekHrs > 140].index, inplace=True)

survey_df['Gender'].value_counts()
# we have problems because we have man/woman multiple times. Let's clean it up 
# We'll remove values containing more than one option to simplify our analysis.
import numpy as np
survey_df.where(~(survey_df.Gender.str.contains(';', na=False)), np.nan, inplace=True)

# print(survey_df.sample())

# DATA VISUALIZATION 
# NOTE: WHEN DRAW AN ADDITIONAL GRAPH, WE NEED TO COMMENT OUT THE PREVIOUS SETTINGS SO THEY DON'T INTERFERE WITH THE NEW ONES
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


sns.set_style('darkgrid')
# matplotlib.rcParams['font.size'] = 14
# matplotlib.rcParams['figure.figsize'] = (9, 5)
# matplotlib.rcParams['figure.facecolor'] = '#00000000'

# print(schema.Country)
# get the first 15 countries of the participants
top_countries = survey_df.Country.value_counts().head(15)
# print(top_countries)
# plot the countries
# plt.figure(figsize=(12,6))
# plt.xticks(rotation=75)
# plt.title(schema.Country) #we can use variables as title
# sns.barplot(x=top_countries.index, y=top_countries)
# plt.show()
sns.countplot(y=survey_df.EdLevel)
plt.xticks(rotation=75);
plt.title(schema['EdLevel'])
plt.ylabel(None);
plt.show()