from dash import html
import dash_bootstrap_components as dbc

tica = [
    dbc.Card(
        [
            html.H4("Physical Scientist and EMT |   Timpanogos Cave National Monument"),
            html.P(
                [
                    html.H5("American Fork, UT"),
                    html.H5("May 2014 - September 2014, April 2015 - October 2015"),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                "Aided in restructuring water sampling objectives. Collected water quality data "
                                "from cave lakes as well as maintained cave lake pressure transducers recording "
                                "lake levels."
                            ),
                            html.Li("Maintained three NOAA meteorology stations in the park."),
                            html.Li(
                                "Participated in Pseudogymnoascus destructans and baseline health surveys for bat "
                                "populations within the park.  Work consisted of mist netting and live captures. "
                                "Experienced handling bats and current on rabies vaccination."
                            ),
                            html.Li(
                                "Participated in cave work outside the park for the Bureau of Land Management and "
                                "Forest Service surveying and inventorying cave resources."
                            ),
                            html.Li(
                                [
                                    "Assisted in creating a 3D laser scan of the cave system.  The resulting 3D model "
                                    "is being used for ",
                                    html.A(
                                        "distance learning (3D Cave Tour)",
                                        href="https://www.nps.gov/tica/learn/photosmultimedia/virtualtour.htm",
                                        target="_blank",
                                    ),
                                    " and resource protection. Results were presented at the GSA 2019 conference.",
                                ]
                            ),
                            html.Li(
                                "EMT responding to medical emergencies and member of the Timpanogos High Angle "
                                "and Cave Rescue Team."
                            ),
                        ]
                    )
                ]
            ),
        ],
        className="card mb-4 border-0",
    )
]
