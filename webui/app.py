# To run this app: python3 index.py
import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
