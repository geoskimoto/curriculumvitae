from dash import html
import dash_bootstrap_components as dbc

skipatrol = [
    dbc.Card(
        [
            html.H4("Ski Patrol |   Park City Mountain Resort"),
            html.P(
                [
                    html.H5('Park City, UT'),
                    html.H5('September 2015 - Janurary 2016'),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li("Rookie patroller responding to trauma and medical emergencies."
                                    ),
                            html.Li("Exposed to handling severe trauma and complex medical situations."
                                    ),
                            html.Li("Trained on toboggans, chair lift evacuation, avalanche safety, avalanche control with explosives, and proper radio and dispatch communications."
                                    ),
                        ]
                    )
                ]
            )
        ]
    )
]













   
