import dash
import pandas as pd
import zipfile

from os import path


surveyZipFileName = 'developer_survey_2019.zip'


def getData() -> pd.DataFrame:
    if not path.exists('assets/data/survey_results_public.csv'):
        zip = zipfile.ZipFile('assets/' + surveyZipFileName)
        zip.extractall('assets/data/')

    return pd.read_csv('assets/data/survey_results_public.csv').drop('Respondent', 1)


def getSchema() -> pd.DataFrame:
    return pd.read_csv('assets/data/survey_results_schema.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
data = getData()
schema = getSchema()
allCountries = data['Country'].dropna().unique()
categoryColumns = data.select_dtypes(exclude=['number', 'datetime']).columns
