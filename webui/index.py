# To run this app: python3 index.py
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app0, app1, app2

app.title = 'Jobs Data Dashboard'

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.H1(children='Jobs Data Dashboard'),
    html.Div([
        dcc.Link('Home', href='/'),
        dcc.Link('App 1', href='/app1'),
        dcc.Link('App 2', href='/app2')
    ], id='header'),

    html.Div(id='page-content'),

    html.Div([
        "Made with Plotly Dash by",
        html.A("Itamar Carvalho",
               href="http://github.com/itamarc",
               target="_blank"),
        "."
    ], id='footer')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app0.layout
    elif pathname == '/app1':
        return app1.layout
    elif pathname == '/app2':
        return app2.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
