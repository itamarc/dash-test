# To run this app: python3 index.py
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home, job_loc, job_tit, sal_loc, sal_tit, prev_loc

app.title = 'Jobs Data Dashboard'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Jobs Data Dashboard', id="h1test"),
    html.Div([
        dcc.Link('Home', href='/', id='home'),
        dcc.Link('Jobs by Location', href='/job_loc', id='job-loc'),
        dcc.Link('Jobs by Title', href='/job_tit', id='job-tit'),
        dcc.Link('Avg Salary by Location', href='/sal_loc', id='sal-loc'),
        dcc.Link('Avg Salary by Job Title', href='/sal_tit', id='sal-tit'),
        dcc.Link('Prevalent Jobs by Location', href='/prev_loc', id='prev-loc')
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
            '/job_loc': 'job-loc',
            '/job_tit': 'job-tit',
            '/sal_loc': 'sal-loc',
            '/sal_tit': 'sal-tit',
            '/prev_loc': 'prev-loc'
        };
        for (var k in map_buttons) {
            if (k == pathname) {
                document.getElementById(map_buttons[k]).className = 'current';
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
        return home.layout
    elif pathname == '/job_loc':
        return job_loc.layout
    elif pathname == '/job_tit':
        return job_tit.layout
    elif pathname == '/sal_loc':
        return sal_loc.layout
    elif pathname == '/sal_tit':
        return sal_tit.layout
    elif pathname == '/prev_loc':
        return prev_loc.layout

    else:
        return '404'


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)
