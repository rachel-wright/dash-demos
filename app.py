import flask
import dash

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H2(children='Hello, Dash')
 ])
 
if __name__ == '__main__':
    app.run_server(debug=True)
 
