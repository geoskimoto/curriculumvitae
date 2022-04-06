from dash import html
import dash_bootstrap_components as dbc

nrcs = [
    dbc.Card(
        [
        html.H4("Hydrologist | USDA Natural Resources Conservation Service"),
        html.P(
            [
                html.H5('Portland, OR'),
                html.H5('October 2020 - Present'),
            ]
        ),
        # dbc.Accordion([
            # dbc.AccordionItem([
                html.P(
                    [
                        html.Ul(
                            [
                                html.Li(
                                    'Project lead for a large data review of all datasets within the jurisdiction of the OR Data Collection Office (ORDCO).'
                                        ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                'Discovered hundreds of errors adversely affecting central tendency statistics through numerous anomaly ' 
                                                'detection tests (logical tests, statistical tests, visual tests, and regression) and evaluated stations for changes '
                                                'in data collection after major disturbance events (e.g. fires, logging).'
                                            )
                                        ]
                                    ),
                                html.Li(
                                    'Built regression web app tool to quickly estimate missing or bad data saving hundreds of hours of staff time and providing '
                                    'a more consistent, accurate, and defensible means at estimating data than previous methods.'
                                ),
                                html.Li(
                                    'Actively review daily data from all WA SNOTEL stations looking for sensor errors/failures.  Additionally, creating a passive '
                                    'notification system and dashboard to automatically alert editors to anomalies.'
                                ),
                                html.Li(
                                    'Maintain and repair SNOTEL weather stations throughout OR and WA.'
                                ),
                                html.Li(
                                    'Assist in authoring monthly Water Supply Outlook Reports (WSOR)'
                                ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                'Maintain and run Visual Basics for Applications scripts to produce reports. Currently rewriting and upgrading '
                                                'report to include better technologies and increase efficiency.'
                                            )
                                        ]
                                    )
                            ]
                        )
                    ]
                )
        ]
    )
]




#
# ●
# ○
# ●
# ●
# ●
# ●
# ○
