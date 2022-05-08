from dash import html
import dash_bootstrap_components as dbc

kinross_exploration = [
    dbc.Card(
        [
            html.H4("Exploration Geologist Intern | Kinross Gold Corporation"),
            html.P(
                [
                    html.H5("Reno, NV"),
                    html.H5("April 2011 - November 2011"),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                "Regional mineral exploration in NV, UT, ID looking for a new significant gold "
                                "deposit in order to continue Kinross’s mining presence in North America.",
                            ),
                            html.Li(
                                "Position included researching historical mining presence and geology of specific "
                                "locations, and physical prospecting of identified locations for mineral wealth. "
                            ),
                            html.Li(
                                "Co-managed an exploration drill program in Austin, NV. Responsible for "
                                "communicating operations with drill rigs, surveyed new roads, drill pads, and "
                                "sumps.  Logged rock chips that were produced from drilling for "
                                "indications of mineralization."
                            ),
                        ]
                    )
                ]
            ),
        ],
        className="card mb-4 border-0",
    )
]


kinross_hydro_intern = [
    dbc.Card(
        [
            html.H4("Hydrologist Intern | Kinross, Round Mountain Gold"),
            html.P(
                [
                    html.H5("Round Mountain, NV"),
                    html.H5("May 2010 - August 2010"),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                "Collected hydrologic data from dozens of monitoring wells and streams from around "
                                "the mine site property and surrounding drainages."
                            ),
                            html.Li(
                                "Familiarized with hydrologic data collection and analysis relating to mine "
                                "operations and objectives. Gained experienced measuring volumetric discharge, "
                                "stage and groundwater levels using acoustic sounders and pressure transducers."
                            ),
                            html.Li(
                                "Created hydrographs from the collected discharge and stage data to assist in "
                                "dewatering efforts."
                            ),
                            html.Li(
                                "Collected water quality samples from monitoring wells around heap leaching "
                                "operations to insure environmental compliance and prevention of cyanide "
                                "leakage into the local basin-fill aquifer."
                            ),
                            html.Li("Installed pressure transducers and loggers in new monitoring wells."),
                        ]
                    )
                ]
            ),
        ],
        className="card mb-4 border-0",
    )
]
