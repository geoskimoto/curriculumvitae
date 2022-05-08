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
    variant="dark",
)

snotel_regr_tool = [
    dbc.Card(
        [
            html.H1(["Snotel Regression Tool"]),
            html.P(
                [
                    html.Ul(
                        [
                            html.Hr(),
                            html.Li(
                                [
                                    "Demonstration version of this application can be found ",
                                    html.A(
                                        "here.",
                                        href="https://snotel-regression-tool.herokuapp.com/",
                                        target="_blank",
                                    ),
                                ]
                            ),
                            html.Li(
                                [
                                    "Login (username: user, password: snotel).  ",
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    "Note - may take up to 40s to load initially as server needs to"
                                                    " start up."
                                                ]
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            html.Hr(),
                            html.Li(
                                html.P(
                                    "The USDA Natural Resources Conservation Service maintains over 900 snow"
                                    " telemetry (SNOTEL) snowpack measuring stations throughout the western United"
                                    " States.  Mountain environments are tough on snowpack and precipitation measuring"
                                    " sensors.  These sensors regularly fault producing erroneous or missing data.  As"
                                    " such published guidelines are used to estimate suspect data.  This tool expands"
                                    " on these guidelines automating much of the process and providing the ability  to"
                                    " build much more robust, accurate, consistent, and defensible regression models.",
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Data is realtime - connected to the National Weather and Climate Center's Air and"
                                    " Water and SNOTEL databases through an API."
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Several regression models available to estimate values: lasso, huber, kernel"
                                    " methods (rbf) with support-vector machines, and decision tree methods (Random"
                                    " Forest, Adaboost, XGBoost)."
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Well fit models and their configurations can be serialized and saved to a sql"
                                    " database.  An API is currently being built that will deliver estimates quickly"
                                    " and automatically using these predetermined models to other applications."
                                )
                            ),
                            html.Hr(),
                            html.A(
                                "Code from Github Repository",
                                href="https://github.com/geoskimoto/snotel-regression-tool-demo-version",
                                target="_blank"
                            ),
                            html.Hr(),
                        ]
                    )
                ]
            ),
        ],
        className="card mx-auto border-0",
    ),
    html.Div([regr_carousel]),
    # dbc.Card([
    #     html.Embed(src='https://snotel-regression-tool.herokuapp.com/',
    #                style={'width':'100%', 'height': '75vw'}
    #                )
    # ])
]
