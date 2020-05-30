import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output
from app import app, data, schema, filterData


class PieChartComponent:
    @staticmethod
    def render(id: str, columns: list, defaultColumn: str):
        @app.callback(
            Output(id + '--graph', 'figure'),
            [Input(id + '--dropdown', 'value'), Input('config-store', 'data')]
        )
        def getData(columnName, configStore):
            filtered = filterData(data, configStore)
            groupedByValues = filtered[columnName].dropna().str.split(
                ';').explode().value_counts().to_frame('counts')

            return {
                'data': [
                    {
                        'type': 'pie',
                        'labels': groupedByValues.index,
                        'values': groupedByValues['counts'],
                        'textposition': 'inside',
                        'textinfo': 'percent+label',
                        'showlegend': False
                    }
                ]
            }

        @app.callback(
            Output(id + '--question', 'children'),
            [Input(id + '--dropdown', 'value')]
        )
        def getQuestion(columnName):
            return schema[schema['Column'] == columnName].values[0][1]

        return html.Div(
            id=id,
            className='piechart-component panel',
            children=[
                dcc.Dropdown(
                    id=id + '--dropdown',
                    className='piechart-component--dropdown',
                    options=[
                        {'label': x, 'value': x} for x in columns
                    ],
                    value=defaultColumn,
                    clearable=False
                ),
                html.P(
                    schema[schema['Column']
                           == defaultColumn].values[0][1],
                    id=id + '--question',
                    className='piechart-component--question'
                ),
                dcc.Loading(
                    dcc.Graph(
                        id=id + '--graph',
                    ),
                    type='circle'
                )
            ]
        )
