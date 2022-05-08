from dash import html

publications = html.Div(
    [
        html.Br(),
        html.H2("Publications", style={"margin": "25px", "text-align": "center"}),
        html.Hr(
            style={
                "height": "2px",
                "width": "30%",
                "background": "teal",
                # 'margin': '15px',
                # 'align':'center'
                "margin-left": "35%",
                "margin-right": "35%",
            }
        ),
        html.Br(),
        html.Br(),
        html.Ul(
            [
                html.Li(
                    html.P(
                        [
                            "Co-author of the monthly ",
                            html.A(
                                "Water Supply Outlook Report",
                                href="https://www.nrcs.usda.gov/wps/portal/nrcs/detail/or/snow/?cid=nrcseprd1721654",
                                target="_blank",
                            ),
                            " for the state of Oregon.",
                        ]
                    )
                ),
                html.Li(
                    html.P(
                        "Miller, A. E., Steele, N. E, Tobin B. W., 2018, Vulnerability and Fragility Risk "
                        "Indices for Non-Renewable Resources,  Journal of Environmental Monitoring"
                    )
                ),
                html.Li(
                    html.P(
                        "N. E. Steele, Cave Climate Characterization and Examining the Effectiveness of Cave "
                        "Management Practices- Timpanogos Cave National Monument, 2016, Geologic Society of "
                        "America, Conference Paper"
                    )
                ),
                html.Li(
                    html.P(
                        "LaSala, B.N., Kemeny, J.M., Levine, J.A., Swetnam, T., Kazhdan, M., Steele, N.E., "
                        "Mckinney, C., Armstrong, A., 2019, Creating a High Resolution Model of the Timpanogos "
                        "Cave System using a Terabyte Scale Lidar Dataset, GSA Annual Meeting in Phoenix, "
                        "Arizona, USA-2019. GSA"
                    )
                ),
                html.Hr(
                    style={
                        "height": "1px",
                        "background": "teal",
                        "margin": "15px 0px 15px",
                    }
                ),
                html.Li(
                    html.P(
                        "Publications I have been heavily involved in either through extensive field work "
                        "and/or data analysis.  Most of these publications directly acknowledge my work."
                    )
                ),
                html.Ul(
                    [
                        html.Li(
                            html.P(
                                "Jones, C. R., Springer, A. E., Tobin, B. W., Zappitello, S. J., Jones, N. A., "
                                "6 November 2017, Characterization and hydraulic behaviour of the complex karst "
                                "of the Kaibab Plateau and Grand Canyon National Park, USA, Geological Society, "
                                "London, Special Publications, 466"
                            )
                        ),
                        html.Li(
                            html.P(
                                "LaSala, B. N., 2019, Creating a High-Fidelity Interactive Simulation of the "
                                "Timpanogos Cave System from a Terabyte-Scale Terrestrial LiDAR Dataset "
                                "[published Master’s thesis], University of Arizona"
                            )
                        ),
                        html.Li(
                            html.P(
                                "Tibuleac, I. M., Eneva M., 2011, Seismic Signature of the Geothermal Field at "
                                "Soda Lake, Nevada, from Ambient Noise Analysis, GRC Transactions, Vol. 35"
                            )
                        ),
                        html.Li(
                            html.P(
                                "Tibuleac, I. M., Von Seggern, D. H., Anderson, J. G., Louie, J. N., 2011, "
                                "Development of Methods for Computing Greens Functions from Ambient Noise "
                                "Recorded by Accelerometers, Analog, Broad and Narrow-Band Seismometers, "
                                "Seismometer, Seismological Research Letters Volume 82, Number 5"
                            )
                        ),
                        html.Li(
                            html.P(
                                "Tibuleac, I. M., 2011, A Higher Resolution Seismic Velocity Model in the "
                                "Reno Basin estimated from Ambient - Seismic  Noise, Nevada Seismology Lab"
                            )
                        ),
                    ]
                ),
            ]
        ),
    ]
)

if __name__ == "__main__":
    print("I import publications")
