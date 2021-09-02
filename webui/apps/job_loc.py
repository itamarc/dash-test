from datetime import date
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import data_source as ds

data = ds.get_jobs_by_location()

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="europe",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue",
    showland=True, landcolor="khaki",
    showocean=True, oceancolor="LightBlue"
)
fig.update_layout(height=500, margin={"r": 0, "t": 0, "l": 0, "b": 0})

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
                max_date_allowed=date(2017, 9, 19),
                initial_visible_month=date(2021, 8, 1),
            )], className='date_range_select'),
    ], className='options_container'),
    dcc.Graph(
        id='jobs-by-location',
        figure=fig
    )
])
