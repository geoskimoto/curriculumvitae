from dash import html
other_projects = [

    html.H1(["Other Projects"]),
    html.Br(),
    html.H3('Many Projects have not yet made it to this CV including the following:'),
        html.Ul([
            html.Li(
                'SNOTEL Change Detection - project in which Double Mass Analysis is automated to detect changes in data collection at SNOTEL weather stations after significant disturbance'
                'events (e.g. fires or logging).'
            ),
            html.Li(
                'SNOTEL Anomaly Detection Toolset - toolset created to detect anomalies through logical tests based on domain knowledge, statistics/ML tests (Isolation Forests, Local'
                'Outlier Factor, Hampel Filter, Z Score) and building regression models that would reveal strong outliers.'
                    ),
            html.Li(
                'Precipitation Response Analysis - study using strong localized monsoon storms as a tracer to determine flow paths and travel times from sinkholes on the Kaibab Plateau '
                'to springs within the Grand Canyon.'
            ),
            html.Li(
                'Phantom Ranch Groundwater Model - model built to assess proposed well water withdrawal on the Bright Angel Creek in the Grand Canyon, AZ and the Colorado River.'
            ),
            html.Li(
                'This website.'
            )
        ]),
    html.H3('Please email me for further explanation and a code preview.')
]

