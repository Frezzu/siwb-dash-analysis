import dash_html_components as html
import dash_core_components as dcc

import dash_table

from dash.dependencies import Input, Output
from app import app, data, filterData


class DataViewer:
    @staticmethod
    def render():
        allColumns = data.columns

        return html.Div([
            html.H2('Data preview'),
            dcc.Loading(
                dash_table.DataTable(
                    id='dataviewer-datatable',
                    columns=[{'name': i, 'id': i} for i in allColumns],
                    data=data[:20].to_dict('records'),
                )
            )
        ])


@app.callback(
    Output('dataviewer-datatable', 'data'),
    [Input('config-store', 'data')]
)
def _updateDataTable(configStore):
    return filterData(data, configStore)[:20].to_dict('records')
