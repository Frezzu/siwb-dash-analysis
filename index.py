# -*- coding: utf-8 -*-

import os
import dash

import dash_core_components as dcc
import dash_html_components as html

from app import app, data, categoryColumns
from components.data_viewer import DataViewer
from components.years_of_code_component import YearsOfCodeComponent
from components.pie_chart_component import PieChartComponent


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
        html.Div(
            [
                YearsOfCodeComponent.render(),
            ],
            className='first-section'
        ),
        html.Div(
            [
                PieChartComponent.render(
                    'OpSys', categoryColumns, 'OpSys'),
                PieChartComponent.render(
                    'DevEnviron', categoryColumns, 'DevEnviron'),
                PieChartComponent.render(
                    'Containers', categoryColumns, 'Containers')
            ],
            className='piecharts-container'
        ),
        DataViewer.render()
    ],
    className='app-container',
)

if __name__ == '__main__':
    appPort = os.environ.get('PORT', 8050)
    app.run_server(host='0.0.0.0', port=appPort, debug=False)
