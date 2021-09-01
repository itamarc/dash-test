# To run this app: python3 index.py
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app0, app1, app2, app3, app4, app5

app.title = 'Jobs Data Dashboard'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Jobs Data Dashboard', id="h1test"),
    html.Div([
        dcc.Link('Home', href='/', id='home'),
        dcc.Link('Jobs by Location', href='/app1', id='job-loc'),
        dcc.Link('Jobs by Title', href='/app2', id='job-tit'),
        dcc.Link('Avg Salary by Location', href='/app3', id='sal-loc'),
        dcc.Link('Avg Salary by Job Title', href='/app4', id='sal-tit'),
        dcc.Link('Prevalent Jobs by Location', href='/app5', id='prev-loc')
    ], id='header'),
    html.Div(id='page-content'),

    html.Div([
        "Made with ",
        html.A("Plotly Dash",
               href="https://plotly.com/dash/",
               target="_blank"),
        " by",
        html.A("Itamar Carvalho",
               href="http://github.com/itamarc",
               target="_blank")
    ], id='footer'),
    html.Span(id='output-clientside')
])

# TODO: FIX THIS
app.clientside_callback(
    """
    function set_current(pathname) {
        map_buttons = {
            '/': 'home',
            '/app1': 'job-loc',
            '/app2': 'job-tit',
            '/app3': 'sal-loc',
            '/app4': 'sal-tit',
            '/app5': 'prev-loc'
        };
        for (var k in map_buttons) {
            if (k == pathname) {
                document.getElementById(
                    map_buttons[pathname]).className = 'current';
            } else {
                document.getElementById(map_buttons[k]).className = 'notcurr';
            }
        }
        return "";
    }
    """,
    Output('output-clientside', 'children'),
    Input('url', 'pathname')
)


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app0.layout
    elif pathname == '/app1':
        return app1.layout
    elif pathname == '/app2':
        return app2.layout
    elif pathname == '/app3':
        return app3.layout
    elif pathname == '/app4':
        return app4.layout
    elif pathname == '/app5':
        return app5.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)
