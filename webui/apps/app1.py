from datetime import date
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

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
        id='life-exp-vs-gdp',
        figure=fig
    )
])
