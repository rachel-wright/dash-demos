import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('data/reqdata.txt',sep='\t', parse_dates=['Date'])
dfbar = pd.DataFrame({'Reqs': df.groupby(['Date','BU']).size(), 'Openings': df.groupby(['Date','BU'])['Openings'].sum()}).reset_index()
dfs = pd.DataFrame({'count': df.groupby(['Date','BU','ReqType','DIV','Location','Clearance','Group']).size()}).reset_index()

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
    
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4(children='table'),
    generate_table(dfs)
 ])
 
 if __name__ == '__main__':
    app.run_server(debug=True)
