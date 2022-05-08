from dash import html
import dash_bootstrap_components as dbc


geo_skills = html.Div(
    [
        html.H4(
            "Hydrogeology Field Skills",
            style={"margin": "25px", "text-align": "center"},
        ),
        html.P(
            [
                html.Ul(
                    [
                        html.Li(
                            "Water sample collection (Isotopes, Environmental DNA, Ions, biologic samples) and "
                            "operating water quality sondes (Hannah, In-Situ Aqua Trolls)",
                        ),
                        html.Li(
                            "Volumetric discharge using Sontek Flow Tracker, Hach FH950, pygmy, and global water FP311"
                        ),
                        html.Li("Pressure transducers (In-Situ, Hobo, Solinst)"),
                        html.Li(
                            "Multi-sensor data loggers (Campbell Scientific CR1000x and CR10x, ECH2O) and wiring "
                            "single-ended, differential, pulse sensors, and resistance sensors with voltage excitation "
                            "(Bridges)."
                        ),
                        html.Li(
                            "Dye tracing protocols",
                        ),
                        html.Li("Installing stream gages in creeks and caves"),
                        html.Li("Construction and installing weather stations"),
                        html.Li("Power systems: solar panels, solar regulators, and battery banks"),
                        html.Li("Telemetry: Iridium, GOES, Cell, Meteorburst"),
                        html.Li("Geologic Mapping"),
                        html.Li("Geologic and geotechnical logging of drilled core"),
                        html.Li(
                            "Participant in over 50 multi-day backpacking trips to nearly every major drainage in "
                            "Grand Canyon. Very remote and rugged terrain occasionally requiring single rope techniques"
                            " to access field sites."
                        ),
                        html.Li("Experienced in canyoneering, caving, technical rope rescue, and packrafting."),
                    ]
                )
            ]
        ),
    ]
)


ems_certs = html.Div(
    [
        html.H4(
            "EMS Certificates and Trainings",
            style={"margin": "25px", "text-align": "center"},
        ),
        html.P(
            [
                html.Ul(
                    [
                        html.Li("Wilderness EMT, March 2013"),
                        html.Li("Wilderness First Responder, June 2017"),
                        html.Li("AIARE 1: Decision Making in Avalanche Terrain, Januaru 2016"),
                        html.Li(
                            "National Cave Rescue Commission Small Party Assisted Rescue, September 2014, June 2015,"
                            " May 2017"
                        ),
                        html.Li("Naional Cave Rescue Commission Level 1, September 2016"),
                        html.Li("Swift Water Rescue Technician Unit 1, March 2017"),
                        html.Li("Packraft Swiftwater Rescue Training, October 2017"),
                    ]
                )
            ]
        ),
    ]
)

other_certs = html.Div(
    [
        html.H4(
            "Additional Certs and Trainings",
            style={"margin": "25px", "text-align": "center"},
        ),
        html.P(
            [
                html.Ul(
                    [
                        html.Li("NPS Operational Leadership, June 2017"),
                        html.Li("S271 Helicopter Flight Crew Training, April 2022"),
                        html.Li("Wildland Fire Resource Advisor, March 2019"),
                        html.Li("S12 Chainsaw Cert, April 2022 - limbing, bucking, and falling trees"),
                    ]
                )
            ]
        ),
    ]
)


# publications = html.Div(
#     [
#                 html.Ul(
#                     [
#                         html.Li('Miller, A. E., Steele, N. E, Tobin B. W., 2018, Vulnerability and Fragility Risk '
#                                 'Indices for Non-Renewable Resources,  Journal of Environmental Monitoring'
#                                 ),
#                         html.Li('N. E. Steele, Cave Climate Characterization and Examining the Effectiveness of Cave '
#                                 'Management Practices- Timpanogos Cave National Monument, 2016, Geologic Society of '
#                                 'America, Conference Paper'
#                                 ),
#                         html.Li('LaSala, B.N., Kemeny, J.M., Levine, J.A., Swetnam, T., Kazhdan, M., Steele, N.E., '
#                                 'Mckinney, C., Armstrong, A., 2019, Creating a High Resolution Model of the Timpanogos '
#                                 'Cave System using a Terabyte Scale Lidar Dataset, GSA Annual Meeting in Phoenix, '
#                                 'Arizona, USA-2019. GSA'
#                                 ),
#
#                         html.Ul(
#                             [
#                                 html.P(
#                                     'Publications I have been heavily involved in either through extensive field '
#                                    'or analysis of data.  Most of these publications my work is directly '
#                                    'acknowledged.'
#                                 ),
#                                 html.Li(
#                                     'Publications I have been acknowledged in, conducted extensive field work for, '
#                                     'and/or analyzed data.'
#                                 ),
#                                 html.Li(
#                                     'Jones, C. R., Springer, A. E., Tobin, B. W., Zappitello, S. J., Jones, N. A., '
#                                     '6 November 2017, Characterization and hydraulic behaviour of the complex karst '
#                                     'of the Kaibab Plateau and Grand Canyon National Park, USA, Geological Society, '
#                                     'London, Special Publications, 466'
#                                 ),
#                                 html.Li(
#                                     'LaSala, B. N., 2019, Creating a High-Fidelity Interactive Simulation of the '
#                                     'Timpanogos Cave System from a Terabyte-Scale Terrestrial LiDAR Dataset '
#                                     '[published Master’s thesis], University of Arizona.'
#                                 ),
#                                 html.Li(
#                                     'Tibuleac, I. M., Eneva M., 2011, Seismic Signature of the Geothermal Field at '
#                                     'Soda Lake, Nevada, from Ambient Noise Analysis, GRC Transactions, Vol. 35'
#                                 ),
#                                 html.Li('Tibuleac, I. M., Von Seggern, D. H., Anderson, J. G., Louie, J. N., 2011, '
#                                         'Development of Methods for Computing Greens Functions from Ambient Noise '
#                                         'Recorded by Accelerometers, Analog, Broad and Narrow-Band Seismometers, '
#                                         'Seismometer, Seismological Research Letters Volume 82, Number 5.'
#                                         ),
#                                 html.Li('Tibuleac, I. M., 2011, A Higher Resolution Seismic Velocity Model in the '
#                                         'Reno Basin estimated from Ambient - Seismic  Noise, Nevada Seismology Lab'
#                                         )
#                                 ]
#                         )
#                     ]
#                 )
#     ]
# )


credentials = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Accordion(
                    [
                        #     dbc.AccordionItem(
                        #         [
                        #             dbc.Row(
                        #                 dbc.Col(geo_skills)
                        #             )
                        #         ],
                        #         title='Hydrogeology Field Skills'
                        #     ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(ems_certs)),
                            ],
                            title="EMS Certs and Trainings",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(other_certs)),
                            ],
                            title="Additional Certs and Trainings",
                        ),
                        # dbc.AccordionItem([
                        #     dbc.Row(
                        #         dbc.Col(ems_certs)
                        #     ),
                        #     ],
                        #     title='Honors'
                        # ),
                        # dbc.AccordionItem([
                        #     dbc.Row(
                        #         dbc.Col(publications)
                        #     ),
                        #     ],
                        #     title='Publications',
                        #     className="card mb-4 border-0",
                        #
                        #     ),
                    ],
                    className="card mb-4 border-0",
                    always_open=False,
                    # style={'height': '1px',
                    #        'background': 'teal',
                    #        'margin': '15px 0px 15px'
                    #          }
                )
            ]
        )
    ]
)
