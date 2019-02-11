import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import afms_charts
import afms_layout
import afms_utiltities as util

bu='BU'
gp='Group'
xv='Location'
yv='Reqs'
tv='Openings'

raw = pd.read_csv('data/activereqs.txt',sep='\t', parse_dates=['Date'])
pieraw = pd.DataFrame({'Reqs': raw.groupby(['BU','Group']).size(), 'Openings': raw.groupby(['BU','Group'])['Openings'].sum()}).reset_index()
barraw = pd.DataFrame({'Reqs': raw.groupby(['Date','BU','Group','Location']).size(), 'Openings': raw.groupby(['Date','BU','Group','Location'])['Openings'].sum()}).reset_index()

bu_options = [{'label': bu, 'value': bu} for bu in raw[bu].unique()]
age_options = [{'label': gp, 'value': gp} for gp in raw[gp].unique()]
gps = raw[gp].unique()

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)


app.layout = afms_layout.afms_layout(bu_options, age_options)

# BU pie chart filtered by age selected in dropdown
@app.callback(
    dash.dependencies.Output('pie_graph','figure'),
    [dash.dependencies.Input('age_selector', 'value'),
    dash.dependencies.Input('bu_selector', 'value')]
)
def load_bupie(val1, val2):
    if (val1 and val2):
        piedf = pieraw[pieraw[gp].isin(val1) and pieraw[bu].isin(val2)]
    elif (val1):
        piedf = pieraw[pieraw[gp].isin(val1)]
    elif (val2):
        piedf = pieraw[pieraw[bu].isin(val2)]
    else:
        piedf = pieraw
    return afms_charts.bu_pie(piedf, bu, yv)

# Reqs by Location bar filtered by BU dropdown
@app.callback(
    dash.dependencies.Output('main_graph', 'figure'),
    [dash.dependencies.Input('age_selector', 'value'),
    dash.dependencies.Input('bu_selector', 'value')]    
)
def update_figure(val1, val2):
    if (val1 and val2):
        filtered_df = barraw[barraw[gp].isin(val1) and barraw[bu].isin(val2)]
    elif (val1):
        filtered_df = barraw[barraw[gp].isin(val1)]
    elif (val2):
        filtered_df = barraw[barraw[bu].isin(val2)]
    else:
        filtered_df = barraw
    return afms_charts.location_bar(filtered_df, gp, gps, xv, yv, tv)

# Filter bar when pie is clicked
@app.callback(
    dash.dependencies.Output('bu_selector','value'),
    [dash.dependencies.Input('age_selector', 'value'),
    dash.dependencies.Input('pie_graph', 'clickData')]
)
def click_pie(val1, val3):
    if val3:
        newbu=[(pt['label']) for pt in val3['points']]
        update_figure(val1, newbu)
        return newbu
    return 

@app.server.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run_server(debug=True)

