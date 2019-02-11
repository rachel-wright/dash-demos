import dash_core_components as dcc
import dash_html_components as html

def afms_layout(bulist,agelist):
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
                        dcc.Graph(id='pie_graph')
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
                html.Div(
                    [
                        dcc.Graph(id='main_graph')
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
