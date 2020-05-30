# -*- coding: utf-8 -*-

import os
import dash

import dash_core_components as dcc
import dash_html_components as html

from app import app, data, categoryColumns
from components.data_viewer import DataViewer


app.layout = html.Div(
    [
        dcc.Store(id='config-store', data={
            'selectedCountries': [],
            'selectedAgeRange': [],
            'selectedGenders': []
        }),
        html.Div(
            [
                html.H1('StackOverflow Survey 2019'),
                html.P('Authors: Bartłomiej Mroziński, Piotr Pawlik',
                       className='authors')
            ],
            className='app-header'
        ),
        DataViewer.render()
    ],
    className='app-container',
)

if __name__ == '__main__':
    appPort = os.environ.get('PORT', 8050)
    app.run_server(host='0.0.0.0', port=appPort, debug=False)
