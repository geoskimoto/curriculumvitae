from dash import html

other_projects = [
    html.H1(["Other Projects"]),
    html.Br(),
    html.H3("Many Projects have not yet made it to this CV including the following:"),
    html.Ul(
        [
            html.Li(
                html.P(
                    "SNOTEL Change Detection - project in which Double Mass Analysis is automated to detect changes in "
                    "data collection at SNOTEL weather stations after significant disturbance events (e.g. fires or "
                    "logging)."
                )
            ),
            html.Li(
                html.P(
                    "SNOTEL Anomaly Detection Toolset - toolset created to detect anomalies through logical tests based"
                    " on domain knowledge, statistics/ML tests (Isolation Forests, Local Outlier Factor, Hampel Filter,"
                    " Z Score) and building regression models that reveal strong outliers."
                )
            ),
            html.Li(
                html.P(
                    "Precipitation Response Analysis - study using strong localized monsoon storms as a tracer to "
                    "determine flow paths and travel times from sinkholes on the Kaibab Plateau to springs within the "
                    "Grand Canyon."
                )
            ),
            # html.Li(
            #     html.P(
            #         "Phantom Ranch Groundwater Model - model built to assess proposed well water withdrawal on the"
            #         " Bright Angel Creek in the Grand Canyon and the Colorado River."
            #     )
            # ),
            html.Li(
                html.P(
                    [
                        html.A(
                            "Small Projects Collection",
                            href="https://github.com/geoskimoto/small-projects-collection",
                        ),
                        " - collection of various smaller data science projects that were geared more towards"
                        " learning.",
                    ]
                )
            ),
        ]
    ),
    html.H4(
        [
            "Please see my ",
            html.A(
                "github page ",
                href="https://github.com/geoskimoto",
            ),
            "to preview these projects.  Some projects are set to private, so email me if "
            "you would like to see the code or further explanation.",
        ]
    ),
]
