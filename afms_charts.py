import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import afms_utilities as util

def bu_pie(df, bu, val):
    labels = df[bu].values
    trace = [go.Pie(labels=labels, values=df[val].values,
                textinfo='label+value', 
                hoverinfo='label+value', 
                marker=dict(colors=util.bucolors(labels)), 
                opacity=0.7,
                )]
    layout = go.Layout(
                margin={'l': 40, 'b': 200, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest',
                # clickmode='event+select'
            )
    return {'data': trace, 'layout': layout}

def location_bar(df, gp, gps, xv, yv, tv):
    traces = []
    for i in gps:
        traces.append(go.Bar(
            x=df[df[gp] == i][xv],
            y=df[df[gp] == i][yv],
            text=df[df[gp] == i][tv],
            opacity=0.7,            
            name=i,
            # hovertemplate="<b>%{fullData.name}</b><br>" +
            #     "Active Reqs: %{y}<br>" +
            #     "Openings: %{text}<br>" +
            #     "<extra></extra>",
            textposition = 'auto',
            marker=dict(
                color=util.agecolor(i)
                )
        ))

    layout = go.Layout(
                xaxis={'title': 'Location'},
                yaxis={'title': 'Active Reqs', 'range': [0, 5]},
                margin={'l': 40, 'b': 200, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )

    return {
        'data': traces,
        'layout': layout
    }


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def generate_line(name, df, dfg, dfx, dfy, dft):
    return dcc.Graph(
        id=name,
        figure={
            'data': [
                go.Scatter(
                    x=df[df[dfg] == i][dfx],
                    y=df[df[dfg] == i][dfy],
                    text=df[df[dfg] == i][dft],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df[dfg].unique()
            ]#,
            # 'layout': go.Layout(
            #     xaxis={'type': 'log', 'title': xtitle},
            #     yaxis={'title': ytitle},
            #     margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            #     legend={'x': 0, 'y': 1},
            #     hovermode='closest'
            # )
        }        
    )
