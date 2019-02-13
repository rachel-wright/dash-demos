import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

blank_figure = go.Figure(layout=go.Layout(
    xaxis={'visible': False, 'showgrid': False},
    yaxis={'visible': False, 'showgrid': False},
))

def afms_layout(bulist,agelist):
    return html.Div([
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Recruiting', children=recruiting_layout(bulist,agelist)),
            dcc.Tab(label='Billing', children=budget_layout()),
        ]),
    ])

def recruiting_layout(bulist,agelist):
    return html.Div(
        [
            html.Div(
                [
                    html.H1(
                        'Active Requisitions',
                        className='eight columns',
                    ),
                    html.Img(
                        src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                        className='one columns',
                        style={
                            'height': '60',
                            'width': '135',
                            'float': 'right',
                            'position': 'relative',
                        },
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P('Filter by Requisition Age:'),
                            dcc.Dropdown(
                                id='age_selector',
                                options=agelist,
                                multi=True,
                                value=[]
                            )   
                        ],
                        className='four columns'
                    ),
                    html.Div(
                        [
                            html.P('Filter by BU:'),
                            dcc.Dropdown(
                                id='bu_selector',
                                options=bulist,
                                multi=True,
                                value=[]
                            )
                        ],
                        className='eight columns'
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id='pie_graph', figure=blank_figure)
                        ],
                        className='four columns',
                        style={'margin-top': '20'}
                    ),
                    html.Div(
                        [
                            dcc.Graph(id='main_graph', figure=blank_figure)
                        ],
                        className='eight columns',
                        style={'margin-top': '20'}
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        # [
                        #     dcc.Graph(id='sub_pie')
                        # ],
                        className='four columns',
                        style={'margin-top': '20'}
                    ),
                    html.Div(
                        [
                            dcc.Graph(id='sub_graph',figure=blank_figure)
                        ],
                        className='eight columns',
                        style={'margin-top': '20'}
                    ),
                ],
                className='row'
            ),
        ],
        className='ten columns offset-by-one'
    )

def budget_layout():
    return html.H2('hello world')
