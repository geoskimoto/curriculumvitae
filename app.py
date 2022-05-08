from dash import html, dcc
import dash_bootstrap_components as dbc
from views import header, profile, contact, education, publications, fieldskills, skills_buttons
from Portfolio import projects_dropdown
from Experience import Experience
from dbs import app

app.layout = dbc.Container(
    [
        html.Div(
            [
                dcc.Location(id='url', refresh=False),
            ]
        ),
        html.Div(
            [
                header,
                # profile.profile
            ]
        ),
        html.Div(contact.contact),
        html.Br(),
        dbc.Col(
            children=[
                dbc.Tabs(
                    children=[
                        dbc.Tab(
                            label="Experience",
                            children=[
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.Div(
                                                [Experience]
                                            ),
                                        ),
                                        dbc.Col([
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        html.Div([education.education])
                                                    )
                                                ]
                                            ),
                                            html.Hr(
                                                style={'height': '1px',
                                                       'background': 'teal',
                                                       'margin': '15px 0px 15px'
                                                       }
                                            ),
                                            dbc.Row([
                                                dbc.Row([
                                                    dbc.Col(
                                                        html.Div(
                                                            [
                                                                html.H4('Developer Skills',
                                                                    style={
                                                                        'margin':'10px',
                                                                        'text-align': 'center'
                                                                    }
                                                                ),
                                                                html.Br(),
                                                                skills_buttons,
                                                                html.Br(),
                                                                html.P([
                                                                    'Hover over points to see stack and abilities.'
                                                                ],
                                                                    style={'text-align': 'center'})
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Col(id='my-skills',
                                                            children=[
                                                                html.Div(
                                                                    id='rose-fig',
                                                                    children=[],
                                                                    style={
                                                                        # "width": "600px",
                                                                        # "height": "400px",
                                                                        "margin": "auto",
                                                                        # 'textAlign': 'center',
                                                                        # 'align': 'center',
                                                                        # "display": "inline-block",
                                                                        # 'display': 'flex',
                                                                        # 'justify-content': 'center',
                                                                        # "border": "3px #5c5c5c solid",
                                                                        # "padding-top": "5px",
                                                                        # "padding-left": "1px",
                                                                        # "overflow": "hidden"
                                                                    }
                                                                ),
                                                                dcc.Tooltip(id="graph-tooltip")
                                                            ],
                                                            )
                                                    ]
                                                ),


                                                html.Hr(
                                                    style={
                                                        'height': '1px',
                                                        'background': 'teal',
                                                        'margin': '15px 0px 15px'
                                                        }
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.Div([fieldskills.geo_skills])
                                                        )
                                                    ]
                                                ),


                                                html.Hr(
                                                    style={'height': '1px',
                                                           'background': 'teal',
                                                           'margin': '15px 0px 15px'
                                                           }
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.Div([fieldskills.ems_certs])
                                                        ),
                                                    ]
                                                ),


                                                html.Hr(
                                                    style={
                                                        'height': '1px',
                                                        'background': 'teal',
                                                        'margin': '15px 0px 15px'
                                                         }
                                                ),

                                                dbc.Row([
                                                    dbc.Col(
                                                        html.Div([fieldskills.other_certs])
                                                    )
                                                    ]
                                                ),


                                                html.Hr(
                                                    style={
                                                        'height': '1px',
                                                        'background': 'teal',
                                                        'margin': '15px 0px 15px'
                                                        }
                                                )
                                            ])
                                        ],
                                            width=4
                                        )
                                        ]
                                )
                                ]
                        ),

                        dbc.Tab(
                            label="Coding Portfolio",
                            children=[
                                dbc.Row(
                                    dbc.Col(
                                        [
                                            html.Br(),
                                            html.Div([projects_dropdown]),
                                            html.Br(),
                                            html.Div(id='projects-div'),
                                        ]
                                    )
                                ),
                            ],
                        ),


                        dbc.Tab(
                            [
                                dbc.Row(
                                    dbc.Col(
                                        [
                                            html.Div([publications.publications])
                                        ]
                                    )
                                )
                            ],
                            label="Publications"
                        )


                    ]
                ),
            ]
        ),
    ],
    fluid=True
    # class_name='container-md'
)
app.title = "NSteele CV"
server = app.server


if __name__ == '__main__':
    app.run_server(debug=False)


