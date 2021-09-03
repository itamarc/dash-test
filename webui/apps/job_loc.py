from app import app
from datetime import date
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import data_source as ds
from dash.dependencies import Input, Output

fig = go.Figure(go.Scattergeo())

layout = html.Div([
    html.Div([
        html.Span([
            dcc.Dropdown(
                id='job-title-dropdown',
                options=[
                    {'label': 'Software Engineer Senior',
                     'value': 'software-engineer-senior'},
                    {'label': 'Software Engineer Junior',
                     'value': 'software-engineer-junior'},
                    {'label': 'Backend Developer',
                     'value': 'backend-developer'}
                ],
                value=''
            )], className='job_name_select'),
        html.Span([
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(1995, 8, 5),
                max_date_allowed=date(2021, 9, 19),
                start_date=date(2021, 8, 3),
                end_date=date(2021, 9, 3),
                initial_visible_month=date(2021, 8, 1),
            )], className='date_range_select'),
    ], className='options_container'),
    dcc.Graph(
        id='jobs-by-location',
        figure=fig
    )
])


@app.callback(
    Output('jobs-by-location', 'figure'),
    Input('job-title-dropdown', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_graph(job_title, start_date, end_date):
    data = ds.get_jobs_by_location(job_title, start_date, end_date)
    fig.update_geos(data,
                    visible=False, resolution=110, scope="europe",
                    showcountries=True, countrycolor="Black",
                    showsubunits=True, subunitcolor="Blue",
                    showland=True, landcolor="LightGrey",
                    showocean=True, oceancolor="LightBlue"
                    )
    fig.update_layout(height=500, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig
