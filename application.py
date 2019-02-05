import dash

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Hello Dash')
])
