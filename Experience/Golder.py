from dash import html
import dash_bootstrap_components as dbc

golder = [
    dbc.Card(
        [
            html.H4("Field Geologist  |   Golder Associates"),
            html.P(
                [
                    html.H5("Reno, NV"),
                    html.H5("February 2012 - March 2015"),
                ]
            ),
            # dbc.Accordion([
            #     dbc.AccordionItem([
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                "Worked independent of other Golder employees with little oversight working up to three"
                                " weeks in the field at a time."
                            ),
                            html.Li(
                                "Responsible for collecting geotechnical data for slope stability assessments regarding"
                                " large open-pit and underground operations. Data included rock strength information"
                                " and information on geological structures (faults, joints, other discontinuities)."
                            ),
                            html.Li(
                                "Collected drill hole data for geologic structure orientations using the software"
                                " WellCAD."
                            ),
                            html.Li(
                                "Provided high quality data products that kept to the standards of Golder Associates"
                                " and clients."
                            ),
                            html.Li(
                                "Effectively communicated and discussed day-to-day operations, progress, issues, and"
                                " goals with clients."
                            ),
                            html.Li(
                                "Top chargeable employee in the Reno Office remaining nearly 100% chargeable throughout"
                                " my time with the firm."
                            ),
                        ]
                    )
                ]
            )
            #     ])
            # ])
        ],
        className="card mb-4 border-0",
    )
]
