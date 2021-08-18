import dash_html_components as html

layout = html.Div([
    html.P("This app is a jobs dashboard with data grabbed from:"),
    html.Ul([
        html.Li(html.A("The Muse",
                       href="https://www.themuse.com/",
                       target="_blank"))
    ]),
], id="page-content")
