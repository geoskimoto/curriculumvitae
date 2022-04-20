from dash import html, dcc
import dash_bootstrap_components as dbc

regr_carousel = dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "https://i.ibb.co/HY1RVmJ/regr-tool-train.png",
            # "img_class_name": 'd-block w-50',
            # "img_style": {
            #     "width":"50%",
            #     "height": "75vw"
            # }
        },
        {
            "key": "2",
            "src": "https://i.ibb.co/f95c70c/regr-tool-results.png",
            # "img_class_name": 'center'
            # 'img_style': {
            #         'border-radius': '10%',
            #         'display': 'block',
            #         'margin-left': 'auto',
            #         'margin-right': 'auto',
            #         'width': '50%',
            # }
        },
        {
            "key": "3",
            "src": "https://i.ibb.co/dfwFhVP/regr-tool-map.png",
            "header": "Spatial information provided for choosing predictor sites.",
            # "img_class_name": 'center'
            # 'img_style': {
            #         'border-radius': '10%',
            #         'display': 'block',
            #         'margin-left': 'auto',
            #         'margin-right': 'auto',
            #         'width': '50%',
            # }
        },
        {
            "key": "4",
            "src": "https://i.ibb.co/jMy877R/regr-tool-db.png",
        },

    ],
    controls=True,
    indicators=True,
    variant='dark'
)

snotel_regr_tool = [
    
    dbc.Card([

        html.H1(["Snotel Regression Tool"]),
        html.P([
            html.Ul([
                html.Hr(),
                html.Li([
                    'Demonstration version of this application can be found ',
                        html.A('here.',
                            href='https://snotel-regression-tool.herokuapp.com/',
                            target='_blank'),
                ]),
                html.Li([
                    'Login - username: user, password: snotel.  Note - may take up to 40s to load initially as server needs to start up.'
                ]),
                html.Hr(),
                html.Li(
                    html.P(
                        "Tool is used to estimate missing or erroneous data from the network of USDA NRCS Snow Telemetry (SNOTEL) snowpack measurement stations using nearby stations and/or other sensors at the same station."
                    )
                ),
                html.Li(
                    html.P(
                        "Data is realtime - connected to the National Weather and Climate Center's Air and Water Database via APIs.)"
                    )
                ),
                html.Li(
                    html.P(
                        "Several options available to estimate the data via regression: linear, kernel trick (rbf) with support-vector machines, and decision tree methods."
                    )
                ),
                html.Li(
                    html.P(
                        "Well fit models and their configurations can be pickeled and saved to a sql database for which a future API will be built to automatically deliver estimates to other applications."
                    )
                ),
                html.Hr(),
                dcc.Link(children=['Code from Github Repository'],
                         href='https://github.com/geoskimoto/snotel-regression-tool'),
                html.Hr()
            ]
            )
            ]
        )
        ]
    ),
    html.Div([regr_carousel]),
    
    # dbc.Card([
    #     html.Embed(src='https://snotel-regression-tool.herokuapp.com/',
    #                style={'width':'100%', 'height': '75vw'}
    #                )
    # ])
    
    
]