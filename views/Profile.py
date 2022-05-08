from dash import html
import dash_bootstrap_components as dbc

profile = dbc.Card(
    [
        # dbc.CardImg(src='', top=True),
        dbc.CardBody(
            [
                html.P(
                    [
                        html.Ul(
                            [
                                html.Li('Dedicated public servant since 2014 serving in both DOI NPS and USDA NRCS.'),
                                html.Li('Experienced leading research and field teams and directly supervising staff. '
                                        'Passionate about leadership and constantly work at making teams healthier, '
                                        'stronger, and ultimately more effective.'
                                        ),
                                html.Li('Experienced hydrologist and data scientist having experience designing, '
                                        'funding, and executing studies.'
                                        ),
                                html.Li('Passion for collecting, managing, analyzing, and communicating data. Possess '
                                        'strong programming skills in Python and R and can perform a multitude of '
                                        'time-series, statistical, machine learning, and geospatial analysis. I '
                                        'additionally can work with SQL relational databases, web development, and can '
                                        'create advanced data visualizations.'
                                        )
                            ]
                        )

                    ]
                )
            ]
        )
    ],
    className="card mb-4 border-0",
)
