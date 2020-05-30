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


def filterGender(genderRow, selectedGenders):
    gendersInRow = str(genderRow).split(';')
    return len(set(gendersInRow) & set(selectedGenders)) > 0


def filterData(data: pd.DataFrame, configStore) -> pd.DataFrame:
    mask = (data['Age'] >= configStore['selectedAgeRange'][0]) & (
        data['Age'] <= configStore['selectedAgeRange'][1])

    if len(allCountries) != len(configStore['selectedCountries']) and len(configStore['selectedCountries']) > 0:
        mask = mask & (data['Country'].isin(configStore['selectedCountries']))

    if len(configStore['selectedGenders']) > 0:
        genderMask = data['Gender'].apply(
            lambda x: filterGender(x, configStore['selectedGenders'])
        )
        mask = mask & genderMask

    return data[mask]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
data = getData()
schema = getSchema()
allCountries = data['Country'].dropna().unique()
categoryColumns = data.select_dtypes(exclude=['number', 'datetime']).columns
