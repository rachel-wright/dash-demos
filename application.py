import dash

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2(children='Hello, World!')
 ])

if __name__ == '__main__':
    app.run_server()

