# -*- coding: utf-8 -*-

import os
import dash

import dash_core_components as dcc
import dash_html_components as html


from app import app, data, categoryColumns


app.layout = html.Div(
    [
        html.H1('Hello world')
    ],
    className='app-container',
)

if __name__ == '__main__':
    appPort = os.environ.get('PORT', 8050)
    app.run_server(host='0.0.0.0', port=appPort, debug=False)
