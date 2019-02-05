import flask
import dash
import dash_html_components as html

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H2(children='Hello, Dash')
 ])
