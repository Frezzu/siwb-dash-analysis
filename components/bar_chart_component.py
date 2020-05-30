import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output
from app import app, data, schema, filterData


class BarChartComponent:
    @staticmethod
    def render(columns):
        id = 'bar-chart-component--' + columns[0] + '--graph'

        @app.callback(
            Output(id, 'figure'),
            [Input('config-store', 'data')]
        )
        def _updateBarChartData(configStore):
            filtered = filterData(data, configStore)
            groupedByValues = [
                {'name': column, 'data': filtered[column].dropna().str.split(';').explode().value_counts().to_frame('counts')} for column in columns
            ]

            return {
                'data': [
                    {
                        'name': column['name'],
                        'type': 'bar',
                                'x': column['data'].index,
                                'y': column['data']['counts']
                    } for column in groupedByValues
                ]
            }

        return html.Div(
            [
                dcc.Loading(
                    dcc.Graph(
                        id=id
                    ),
                ),
                html.Dl(
                    BarChartComponent._getDesc(columns),
                    className='barchart-component--question-wrapper',
                ),
            ],
            className='barchart-component'
        )

    @staticmethod
    def _getDesc(columns):
        theList = []

        for col in columns:
            theList.append(html.Dt(col))
            theList.append(
                html.Dd(schema[schema['Column'] == col].values[0][1]))

        return theList
