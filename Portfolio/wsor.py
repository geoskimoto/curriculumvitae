from dash import html, dcc
import dash_bootstrap_components as dbc


wsor_carousel = dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "https://i.ibb.co/Y8yfXQH/wsor-app1.png",
            # "header": "First two Principal Components and Loadings",
        },
        {
            "key": "2",
            "src": "https://i.ibb.co/hD35dXH/wsor-app2.png",
            # 'header':
            "img_class_name": "d-block w-50"
            # "img_style": {
            #     "width":"50%",
            #     "height": "75vw"
            # }
        },
        {
            "key": "3",
            "src": "https://i.ibb.co/F62zhGS/wsor-app3.png",
            # "header": 'Correlations between each original feature and the principal components themselves.',
        },
        {
            "key": "4",
            "src": "https://i.ibb.co/mD37cPc/wsor-app4.png",
            # "header": "Cummulative Variance Screeplot",
            # "img_class_name": 'center'
            # 'img_style': {
            #         'border-radius': '10%',
            #         'display': 'block',
            #         'margin-left': 'auto',
            #         'margin-right': 'auto',
            #         'width': '50%',
            # }
        },
        # {
        #     "key": "4",
        #     "src": 'https://i.ibb.co/94mpsQT/wsor-app-API.png',
        #     # "header": "Cummulative Variance Screeplot",
        #     # "img_class_name": 'center'
        #     # 'img_style': {
        #     #         'border-radius': '10%',
        #     #         'display': 'block',
        #     #         'margin-left': 'auto',
        #     #         'margin-right': 'auto',
        #     #         'width': '50%',
        #     # }
        # },
    ],
    controls=True,
    indicators=True,
    variant="dark",
)


wsor = [
    dbc.Card(
        [
            html.H1(["Water Supply Outlook Reporting App"]),
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
                                        href="https://wsor-app.herokuapp.com/",
                                        target="_blank",
                                    ),
                                ]
                            ),
                            html.Li(
                                [
                                    "Additionally, using cron, scheduled reports are produced regularly. Their"
                                    " associated static html files are saved to a public server and which can be"
                                    " found ",
                                    html.A(
                                        "here.",
                                        href="https://www.wcc.nrcs.usda.gov/ftpref/support/wsor/2022_4/or/major/",
                                    ),
                                ]
                            ),
                            html.Hr(),
                            html.Li(
                                [
                                    html.P(
                                        "This automated reporting tool pulls snow, precipitation, reservoir, and"
                                        " forecast data from the National Weather and Climate Center's Air-Water and"
                                        " Snow Telemetry databases using a REST API.",
                                        # dbc.Card([
                                        #     html.Img(src='https://i.ibb.co/94mpsQT/wsor-app-API.png',
                                        #     width="300",
                                        #     height="300"
                                        #     )
                                        #     ])
                                    )
                                ]
                            ),
                            html.Li(
                                html.P(
                                    "The app is built using Flask and jinja templating. The data retrieved is"
                                    " automatically organized and compiled in the back end using pandas and converted"
                                    " to html tables. "
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Reports can be generated to show monthly hydro-meteorology measurements, medians,"
                                    " and streamflow forecasts for hydrologic basins within any state of choice for any"
                                    " month-year. Reports are also cached server side for 24hrs to increase performance"
                                    " for common requests."
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Tool replaces legacy excel and vba systems providing a more capable and less error"
                                    " prone system whose codebase is easy to maintain. Additionally, reports are now in"
                                    " a more presentable html framework and can be produced instantly for any"
                                    " month-year."
                                )
                            ),
                            html.Hr(),
                            html.A(
                                "Code from Github Repository",
                                href="https://github.com/geoskimoto/wsor-automated-reporting-demo-version",
                                target="_blank",
                            ),
                            html.Hr(),
                            html.Div([wsor_carousel]),
                        ]
                    )
                ]
            ),
        ],
        className="card mx-auto border-0",
    ),
    # dbc.Card([
    #     html.Embed(src='https://wsor-app.herokuapp.com/',
    #                style={'width': '100%', 'height': '75vw'}
    #                )
    # ])
]
