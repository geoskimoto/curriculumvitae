import os
from pathlib import Path

# from Code_Portfolio import ...
# from Field_Portfolio import ...
# from Intro import intro
from views import Header, Profile, Contact, Education, FieldSkills, skills_buttons
from Portfolio import projects_dropdown
from views.Skills import RoseScatterPlot
from dash.dependencies import Input, Output, State
from Experience import Experience
# from views.Biography import Biography
import base64
from maindash import app
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

image_filename = './P6170205.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# app.title = 'Favicon'
app.title = "NSteele CV"
server = app.server


app.layout = dbc.Container([
    html.Div(
        [
            dcc.Location(id='url', refresh=False),
            # dcc.Link('Navigate to "/"', href='/'),
            # html.Br(),
            # dcc.Link('Navigate to "/page-2"', href='/page-2')
        ]
    ),
    html.Div([Header,
              # dbc.Card(
              #     dbc.Row([
              #         # dbc.Col(
              #         #     html.Img(src='https://lh3.googleusercontent.com/NuT5Hk1fQ5bKoGjA_8Q40Xeh1fTS1nFXh0iqUkNh4z4amjYKWohXit4vguO6-5aRXLH2SMHtmZI9twykSUmgIStc4PjR5OF2oy0Dvzuj9-FJ_8hBQgTghCKsJebYkwkudoIfcvHpVgE=w2400',
              #         #                  height='310px', width='225px'
              #         #                  )
              #         #     ),
              #         dbc.Col(
              #             html.P(
              #                 html.Div([Profile.Profile])
              #                 )
              #             )
              #         ])
              #     ),
              # html.Img(src="https://lh3.googleusercontent.com/YA0Z6b1KlLrs3Wbk5QM3n4mQ6RwqEEwunCObeLSgoqfaBw-CSXUbpD78k0Lq7_hsQa4dKjIvDOqnpIYrpmjczvloymnGQ2JxNB8ZUi4MJ_5IGlVqBOh2gElVqy3ankXSkIeDt0flzT4=w2400?source=screenshot.guru" 
                        # )],
                        
              #html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image.decode))],
              # html.Div([Contact.Contact]),
              ]),
    html.Div(Contact.Contact),
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
                                        html.Div([Experience]
                                                ),
                                        # width=8
                                    ),
                                    dbc.Col([
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    html.Div([Education.Education])
                                                    # html.Plaintext('Education')
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
                                                            html.H4('Computer Skills',
                                                                style={
                                                                    'margin':'10px',
                                                                    'text-align': 'center'
                                                                }
                                                            ),
                                                            html.Br(),
                                                            skills_buttons
                                                        ]
                                                    )
                                                ),
                                                dbc.Col(id='my-skills',
                                                        children=[
                                                            html.Div(id='rose-fig')
                                                        ]
                                                        )
                                                ]
                                            ),
                                            dbc.Row([
                                                dbc.Col(
                                                    html.Div([FieldSkills.FieldSkills])
                                                )
                                                ])








                                        ])
                                    ],
                                    width=5)
                                    ]
                            )
                            ]
                    ),

                    # dbc.Tab(
                    #     label="Skills",
                    #     children=[
                    #         dbc.Row(
                    #             dbc.Row([
                    #                 # dbc.Col(html.Div([skills_buttons]), width=3),
                    #                 dbc.Col(id='my-skills2',
                    #                         children = [
                    #                             html.Div(id='rose-fig2')
                    #                         ])
                    #                          # ]),
                    #             ])
                    #         )
                    #         ]),
                    dbc.Tab(
                        label="Portfolio",
                        children=[
                            dbc.Row(
                                dbc.Col(
                                    [
                                    # html.Br(),
                                    html.Div([projects_dropdown]),
                                    html.Br(),
                                    html.Div(id='projects-div')
                                    ]
                                )
                            ),
                        ],
                    ),
                    
                    
                        ]),
                    ]),
    ])






# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/Experience' or pathname == '/':
#         return Experience
#     elif pathname == '/Skills':
#         return Skills
#         # dbc.Card([
#         #     html.Div([Skills]),
#         #     dcc.Graph(id='figure',
#         #     #           figure=ScatterPlot('DS').scatter_plot(),
#         #     #           config=dict(displayModeBar=False)
#         #               )
#         # ],
#         #     className='col-8')
#     # elif parn Portfoliothname == '/Portfolio':
#     #     #     retu
#
#     # elif pathname == '/dash-financial-report/full-view':
#     #     return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
#     else:
#         return None










if __name__ == '__main__':
    app.run_server(debug=True)

