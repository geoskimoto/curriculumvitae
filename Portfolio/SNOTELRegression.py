from dash import html
import dash_bootstrap_components as dbc


            
snotel_regr_tool = [
    
    dbc.Card([

        html.H1(["Snotel Regression Tool"]),
        html.P([
            html.Ul([
                html.Li("Note: This public version is hosted on a cold server and may take up to 40s to load. Login is username: user, password: snotel"
                ),
                html.Li(
                    "Tool is used to estimated missing or erroneous data from the network of USDA NRCS Snow Telemetry (SNOTEL) snowpack measurement stations using nearby stations and/or other sensors at the same station."
                ),
                html.Li(
                    "Data is realtime - connected to NRCS Air and Water Database via a Rest API (https://api.snowdata.info/) and SOAP API (https://www.nrcs.usda.gov/wps/portal/wcc/home/dataAccessHelp/webService/)"
                ),
                html.Li(
                    "Several options available to estimate the data via regression: linear, kernel trick (rbf), support-vector machines, and decision tree methods."
                ),
                html.Li(
                    "Well fitting models and their configurations can then be pickeled/saved to a sql database for which an API then uses to automatically deliver future estimates to other applications."
                ),
                html.Li(
                    "Please email me if you'd like to see the code base behind this application."
                )
            ]
            )
            ]
        )
        ]
    ),

    
    dbc.Card([
        html.Embed(src='https://snotel-regression-tool.herokuapp.com/',
                   style={'width':'100%', 'height': '75vw'} 
                   )
    ])
    
    
]