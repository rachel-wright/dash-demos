import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import afms_charts
import afms_layout
import afms_utilities as util

bu='BU'
gp='Group'
xv='Location'
yv='Reqs'
tv='Openings'
rfs='RFS'
clin='CLIN'

raw = pd.read_csv('data/activereqs.txt',sep='\t', parse_dates=['Date'])
pieraw = pd.DataFrame({'Reqs': raw.groupby(['BU','Group']).size(), 'Openings': raw.groupby(['BU','Group'])['Openings'].sum()}).reset_index()
barraw = pd.DataFrame({'Reqs': raw.groupby(['Date','BU','Group','Location']).size(), 'Openings': raw.groupby(['Date','BU','Group','Location'])['Openings'].sum()}).reset_index()
fin = pd.read_csv('data/rfs_actuals.txt',sep='\t')

bu_options = [{'label': i, 'value': i} for i in raw[bu].unique()]
age_options = [{'label': i, 'value': i} for i in raw[gp].unique()]
rfs_options = [{'label': i, 'value': i} for i in fin[rfs].unique()]
clin_options = [{'label': i, 'value': i} for i in fin[clin].unique()]
gps = raw[gp].unique()

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

params = {
    'bulist': bu_options,
    'agelist': age_options,
    'rfslist': rfs_options,
    'clinlist': clin_options
}

app.layout = afms_layout.afms_layout(params)

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
    dfr = barraw
    if (val1):
        dfr = dfr[dfr[gp].isin(val1)]
    if (val2):
        dfr = dfr[dfr[bu].isin(val2)]
    return afms_charts.location_bar(dfr, gp, gps, xv, yv, tv)

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

@app.callback(
    dash.dependencies.Output('sub_graph','figure'),
    [dash.dependencies.Input('main_graph','selectedData')]
)
def fill_details(val):
    return afms_charts.generate_details(val)

@app.callback(
    dash.dependencies.Output('fin_graph', 'figure'),
    [dash.dependencies.Input('gp_slider','value'),
    dash.dependencies.Input('rfs_selector','value'),
    dash.dependencies.Input('clin_selector','value')]
)
def fill_findata(val1, val2, val3):
    dff = fin
    gpf = 'RFS'
    if (val1 == 0):
        gpf='CLIN'
    if (val2):
        dff = dff[dff['RFS'].isin(val2)]
    if (val3):
        dff = dff[dff['CLIN'].isin(val3)]
    return afms_charts.generate_fin_bar(dff,gpf)

@app.server.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run_server(debug=True)

