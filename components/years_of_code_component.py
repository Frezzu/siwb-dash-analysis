import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from app import app, data, filterData


class YearsOfCodeComponent:
    @staticmethod
    def render():
        return html.Div(
            [
                html.Div(
                    [
                        html.P('Bins size: '),
                        dcc.Input(
                            id='years-of-code--config-size-of-bins',
                            type='number',
                            value=3
                        )
                    ],
                    className='years-of-code--config'
                ),
                dcc.Loading(
                    dcc.Graph(
                        id='years-of-code--graph'
                    )
                )
            ],
            className='panel'
        )


@app.callback(
    Output('years-of-code--graph', 'figure'),
    [
        Input('years-of-code--config-size-of-bins', 'value'),
        Input('config-store', 'data')
    ],
)
def _yearOfCode_numberOfBinsCallback(sizeOfBin, configStore):
    filtered = filterData(data, configStore)

    return {
        'data': [
            {
                'type': 'histogram',
                'x': filtered['YearsCode'],
                'name': 'Years of coding',
                'xbins': {
                    'size': sizeOfBin
                }
            },
            {
                'type': 'histogram',
                'x': filtered['YearsCodePro'],
                'name': 'Years of professional coding',
                'xbins': {
                    'size': sizeOfBin
                }
            }
        ]

    }
