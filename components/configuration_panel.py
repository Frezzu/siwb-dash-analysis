import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output
from app import app, data, allCountries


class ConfigurationPanel:
    @staticmethod
    def render():
        genders = data['Gender'].dropna().str.split(';').explode().unique()

        return html.Div(
            [
                html.H6('Countries ({}/{})'.format(0, len(allCountries)),
                        id='configuration-panel--selected-countries-header'),
                html.Button('Select all',
                            id='configuration-panel--select-all', n_clicks=0),
                dcc.Dropdown(
                    id='configuration-panel--selected-countries',
                    multi=True,
                    options=[
                        {'label': x, 'value': x} for x in allCountries
                    ],
                    value=[
                        x for x in allCountries[:10]
                    ]
                ),
                html.H6('Age {} - {}'.format(0, 10),
                        id='configuration-panel--selected-age-header'),
                ConfigurationPanel.renderRangeSlider(
                    'Age', 'Age', data['Age'].min(), data['Age'].max(), 1),
                html.H6('Gender'),
                dcc.Checklist(
                    id='configuration-panel--selected-genders',
                    options=[
                        {'label': x, 'value': x} for x in genders
                    ],
                    value=[str(x) for x in genders]
                )
            ],
            className='configuration-panel panel'
        )

    @staticmethod
    def renderRangeSlider(columnName, label, min, max, step):
        d = int((max - min) / 3) + 1
        marks = {int(min): str(int(min)), int(max): str(int(max))}
        marks.update({x * d: str(x * d) for x in range(1, 3)})

        return dcc.RangeSlider(
            id='slider-switch-slider--{}'.format(columnName),
            min=min,
            max=max,
            step=step,
            value=[25, 60],
            marks=marks
        )


@app.callback(
    Output('configuration-panel--selected-countries', 'value'),
    [Input('configuration-panel--select-all', 'n_clicks')],
    prevent_initial_call=True
)
def _selectAllCountries(n_clicks):
    return allCountries


@app.callback(
    Output('config-store', 'data'),
    [
        Input('configuration-panel--selected-countries', 'value'),
        Input('slider-switch-slider--Age', 'value'),
        Input('configuration-panel--selected-genders', 'value')
    ]
)
def _updateStore(selectedCountries, selectedAgeRange, selectedGenders):
    return {
        'selectedCountries': selectedCountries,
        'selectedAgeRange': selectedAgeRange,
        'selectedGenders': selectedGenders
    }


@app.callback(
    Output('configuration-panel--selected-countries-header', 'children'),
    [Input('configuration-panel--selected-countries', 'value')]
)
def _updateSelectedCountriesHeader(selectedCountries):
    return 'Countries ({}/{})'.format(len(selectedCountries), len(allCountries))


@app.callback(
    Output('configuration-panel--selected-age-header', 'children'),
    [Input('slider-switch-slider--Age', 'value')]
)
def _updateSelectedAgeHeader(ageRange):
    return 'Age [{} - {}]'.format(ageRange[0], ageRange[1])
