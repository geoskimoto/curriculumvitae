from maindash import app
from dash.dependencies import Input, Output
from views import Education
from Experience import Experience
from dash import html
import dash_bootstrap_components as dbc
from views.Skills import RoseScatterPlot
server = app.server


#THIS appears to be a copyish of views.__init__.  Don't think it's referenced anywhere?



skills_buttons = html.Div(
                    dbc.ButtonGroup(
                        [
                            dbc.Button(id='btn-nclicks-1',
                                       children='Data Science',
                                       n_clicks=0,
                                       n_clicks_timestamp=-1,
                                       # style=dict(display='block', height='60px', width='200px'),
                                       outline=True,
                                       size='sm',
                                       color="info",
                                       className='btn'),
                            dbc.Button(id='btn-nclicks-2',
                                       children='Other IT',
                                       n_clicks=0,
                                       n_clicks_timestamp=-1,
                                       # style=dict(display='block', height='60px', width='200px'),
                                       outline=True,
                                       size='sm',
                                       color="info",
                                       className='btn'),
                            dbc.Button(id='btn-nclicks-3',
                                       children='Coding',
                                       n_clicks=0,
                                       n_clicks_timestamp=-1,
                                       # style=dict(display='block', height='60px', width='200px'),
                                       outline=True,
                                       size='sm',
                                       color="info",
                                       className='btn'),
                            # dbc.Button(id='project-management-skills',
                            #             children='Project Management Skills',
                            #             n_clicks=0,
                            #             n_clicks_timestamp=-1,
                            #            style=dict(display='block', height='60px', width='200px'),
                            #            className='btn'),
                            dbc.Button(id='btn-nclicks-4',
                                       children='Field Skills',
                                       n_clicks=0,
                                       n_clicks_timestamp=-1,
                                       # style=dict(display='block', height='60px', width='200px'),
                                       outline=True,
                                       size='sm',
                                       color="info",
                                       className='btn'),
                            dbc.Button(id='btn-nclicks-5',
                                       children='EMS',
                                       n_clicks=0,
                                       n_clicks_timestamp=-1,
                                       # style=dict(display='block', height='60px',
                                       #            width='200px'),
                                       outline=True,
                                       size='sm',
                                       color="info",
                                       className='btn')

                        ],
                        vertical=False,
                        size='md'
                    )
)


layout = html.Div([
    dbc.Col(
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
                                            html.H4('Skills',
                                                    style={
                                                        'margin': '10px',
                                                        'text-align': 'center'
                                                    }
                                                    ),
                                            html.Br(),
                                            html.Div([skills_buttons])
                                        ]
                                    )
                                ),
                                dbc.Col(id='my-skills',
                                        children=[
                                            html.Div(id='rose-fig')
                                        ]
                                        )
                                ]
                            )
                        ])
                    ],
                        width=4)
                ]
            )
        ]
)

# @app.callback(Output('rose-fig', 'children'),
#               Input('btn-nclicks-1', 'n_clicks'),
#               Input('btn-nclicks-2', 'n_clicks'),
#               Input('btn-nclicks-3', 'n_clicks'),
#               Input('btn-nclicks-4', 'n_clicks'),
#               Input('btn-nclicks-5', 'n_clicks'),
#               )
# def update_skills(btn_1, btn_2, btn_3, btn_4, btn_5):
#     #    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
#     changed_id = callback_context.triggered[0]['prop_id'].split('.')[0]
#     if 'btn-nclicks-1' in changed_id:
#         skill_selection = 'DS'
#     elif 'btn-nclicks-2' in changed_id:
#         skill_selection = 'Geospatial'
#     elif 'btn-nclicks-3' in changed_id:
#         skill_selection = 'Coding'
#     elif 'btn-nclicks-4' in changed_id:
#         skill_selection = 'Field'
#     elif 'btn-nclicks-5' in changed_id:
#         skill_selection = 'EMS'
#     else:
#         skill_selection = 'DS'
#
#         # use this for troubleshooting. Comment out above line and uncomment this block.
#         # ctx_msg = json.dumps({
#         #    'states': callback_context.states,
#         #    'triggered': callback_context.triggered,
#         #    'inputs': callback_context.inputs
#         # }, indent=2)
#         # return html.Div([html.Pre(ctx_msg),
#         #                 html.Pre(changed_id)])
#
#     # def skills_rose_plot (skill_selection):
#     plot = RoseScatterPlot(skill_selection)
#     plot.rose_scatter_plot()
#     RosePlot = (
#         dbc.Container([
#             html.Div(
#                 children=[
#                     dcc.Graph(
#                         figure=plot.rose_plot,
#                         # responsive=True,
#                         # fluid=True
#                     )
#                 ]
#             )
#         ],
#             fluid=True
#         )
#     )
#
#     return RosePlot