import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

blank_figure = go.Figure(layout=go.Layout(
    xaxis={'visible': False, 'showgrid': False},
    yaxis={'visible': False, 'showgrid': False},
))

figure_config = {
        'displayModeBar': False
    }

def afms_layout(params):
    return html.Div([
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Recruiting', children=recruiting_layout(params)),
            dcc.Tab(label='Billing', children=budget_layout(params)),
        ]),
    ])

def recruiting_layout(params):
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
                                options=params['agelist'],
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
                                options=params['bulist'],
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
                            dcc.Graph(id='pie_graph', figure=blank_figure, config=figure_config)
                        ],
                        className='four columns',
                        style={'margin-top': '20'}
                    ),
                    html.Div(
                        [
                            dcc.Graph(id='main_graph', figure=blank_figure, config=figure_config)
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
                            dcc.Graph(id='sub_graph',figure=blank_figure, config=figure_config)
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

def budget_layout(params):
    return html.Div(
        [
            html.Div(
                [
                    html.H1(
                        'Contract Spending',
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
                            html.P('Group by:')                  
                        ],
                        className='four columns'
                    )
                ],
                className='row'
            ),            
            html.Div(
                [
                    html.Div(
                        [
                            dcc.RadioItems(id='gp_slider',
                                        options=[{'value': 0, 'label': 'CLIN'},{'value': 1, 'label': 'RFS'}],
                                        value=0,
                                        labelStyle={'display': 'inline-block'}
                                        )
                            # dcc.Slider(
                            #                     id='gp_slider',
                            #                     min=0,
                            #                     max=1,
                            #                     step=1,
                            #                     value=0,
                            #                     marks={0: 'CLIN', 1: 'RFS'},
                            #                     included=False
                            #                 )
                            # html.Table(
                            #     [html.Tr(
                            #         [html.Td(html.P('CLIN')),
                            #         # dcc.Checklist(id='gp_selector', options=[{'label': '', 'value': 'CLIN'}], values=['CLIN']),
                            #         # html.Td(html.Label([
                            #         #                 dcc.Input(id='gp_selector', type='checkbox'),
                            #         #                 html.Span(className='slider switch round')
                            #         #             ],
                            #         #             className='switch')),                                    
                            #         html.Td(html.P('RFS'))]
                            #     )]
                            # )                            
                        ],
                        className='two columns',
                        style={'margin-left': '20', 'margin-bottom': '40'}
                    )
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div([html.P('Filter by RFS:')], className='four columns'),
                    html.Div([html.P('Filter by CLIN:')], className='four columns'),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='rfs_selector',
                                options=params['rfslist'],
                                multi=True,
                                value=[]
                            )   
                        ],
                        className='four columns'
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='clin_selector',
                                options=params['clinlist'],
                                multi=True,
                                value=[]
                            )
                        ],
                        className='four columns'
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id='fin_graph', figure=blank_figure, config=figure_config)
                        ],
                        className='eight columns',
                        style={'margin': '20'}
                    ),
                    # html.Div(
                    #     [
                    #         dcc.Graph(id='graph2', figure=blank_figure, config=figure_config)
                    #     ],
                    #     className='four columns',
                    #     style={'margin': '20'}
                    # ),
                ],
                className='row'
            ),
            # html.Div(
            #     [
            #         html.Div(
            #             [
            #                 dcc.Graph(id='graph3',figure=blank_figure)
            #             ],
            #             className='six columns',
            #             style={'margin-top': '20'}
            #         ),
            #         html.Div(
            #             [
            #                 dcc.Graph(id='graph4',figure=blank_figure)
            #             ],
            #             className='six columns',
            #             style={'margin-top': '20'}
            #         ),
            #     ],
            #     className='row'
            # ),
        ],
        className='ten columns offset-by-one'
    )