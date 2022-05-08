from dash import html, dcc
import dash_bootstrap_components as dbc

PCA = dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "https://lh3.googleusercontent.com"
            "/zDu2QO6UXSKzkJPwqsHSFjAwJ2dIqwKItR8Dop5Z2A5AWkRD5xCrRDiHcYbScIDyWba96qa3a65A9xDWYaWCao4KfCsfXdhKkTFpj7tyyIxvtdy4jgAm13OT3Mvu3brBHmkjQZrtbZk=w2400",
            "header": "First two Principal Components and Loadings",
        },
        {
            "key": "2",
            "src": "https://lh3.googleusercontent.com"
            "/BUJCYRgyFbcsHFW56kELO0i58FoDqRvbsunylVZvZ4TPxIL8pQBDkKbYP5P6EgJjjIJU"
            "-J2JZndv0YIpqHkvGSsCxED_QooQHf9mV4RJhSoUn9nRjaJM4mVrLYcz39RrKSM6HjhQVUQ=w2400",
            # "header": "Image from Wood, A.J., 2019, Hydrogeology of the Coconino Aquifer, Kaibab Plateau, Grand Canyon, AZ",
            "img_class_name": "d-block w-50"
            # "img_style": {
            #     "width":"50%",
            #     "height": "75vw"
            # }
        },
        {
            "key": "3",
            "src": "https://lh3.googleusercontent.com/-CDvzPGOr1vJT_oDr3LAVcYTwkvT5RTaiRWEcO4ylKcxq8Q4aQp_YoByr-NkOUn"
            "-MuIh0M41ABkpJsauP3Peaj3VLXnXjNe8G8OXYZNvMmracVZ83rL23pvc4zBIUvfN5SFV3u7t-os=w2400",
            "header": "Correlations between each original feature and the principal components themselves.",
        },
        {
            "key": "4",
            "src": "https://lh3.googleusercontent.com/QXumJxUypNBlqmhrxzGdE0sK3ME0aArkW2r_kdP"
            "-B1t0pjqtfQtnpU163EHkbjY0V0vaKkYWGH7SndkPdJ9N53eDfN5s0HvTW"
            "-b7BDAoIjFHuyFR6eVcyTSSkS4Bw9hIOmCzjfJwQso=w2400",
            # "header": "Cummulative Variance Screeplot",
            # "img_class_name": 'center'
            # 'img_style': {
            #         'border-radius': '10%',
            #         'display': 'block',
            #         'margin-left': 'auto',
            #         'margin-right': 'auto',
            #         'width': '50%',
            # }
        },
    ],
    controls=True,
    indicators=True,
    variant="dark",
)

Cluster = []

kp_waterchem = [
    dbc.Card(
        [
            html.H1(
                "Clustering of water chemistry data from springs on the Kaibab Plateau, north of the Grand "
                "Canyon, AZ"
            ),
            html.Hr(),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                html.P(
                                    "Project repeated Principal Component Analysis initially conducted by "
                                    "Wood, Alexander, 2019, Hydrogeology of the Coconino Aquifer on the Kaibab Plateau, Grand Canyon, "
                                    "Arizona, Northern Arizona University, Flagstaff, AZ, USA. "
                                    "Data also acquired from Alex's thesis."
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Additionally, the relationships between springs was further explored through additional "
                                    "representative learning clustering methods: kmeans+, gaussian, and hierarchical."
                                )
                            ),
                            html.Li(
                                html.P(
                                    "Overarching goal was to identify springs that have similar ionic and isotopic chemistry and "
                                    "therefore discover evidence "
                                    "of connected flow paths and similar origins. Please see Alex's thesis for results which this "
                                    "analysis further supports. "
                                )
                            ),
                        ]
                    ),
                    html.Hr(),
                    html.A(
                        children=["Code from Github Repository"],
                        href="https://github.com/geoskimoto/kb-spring-chemistry-clustering/blob/master/KaibabPlateau-SpringWaterChem-Cluster%2BPCA.ipynb",
                        target="_blank"
                    ),
                    html.Hr(),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col([PCA]),
                ]
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    html.Br(),
                                    html.H3(
                                        "Hierarchical clustering visual of Kaibab Plateau spring water chemistry"
                                    ),
                                    html.Img(
                                        src="https://lh3.googleusercontent.com/ch8n3yJXBBf9H"
                                        "-G3lWSpEcDwNdy4FmESV5MkDWzcD6oGI4PTvHWaotN8_IwqJ2h2zWTsJRbv_z2xaVeue"
                                        "-5L_mRyUdWCBfB5ctFdSEsOXvAxS-rOMe3CvACbanHWZqLgCacNWEeAQl4=w2400",
                                        height="100%",
                                        width="65%",
                                    ),
                                    # html.Figcaption(['Hierarchical clustering visual of Kaibab Plateau spring water chemistry'
                                    #                 ]),
                                ],
                                # fluid=True,
                            )
                        ]
                    )
                ]
            ),
        ],
        className="card border-0", #mx-auto
    )
]

#                 dbc.Row([
#                     dbc.Col([
#                         dbc.Container([
#                         html.Img(src="https://lh3.googleusercontent.com/ch8n3yJXBBf9H-G3lWSpEcDwNdy4FmESV5MkDWzcD6oGI4PTvHWaotN8_IwqJ2h2zWTsJRbv_z2xaVeue-5L_mRyUdWCBfB5ctFdSEsOXvAxS-rOMe3CvACbanHWZqLgCacNWEeAQl4=w2400",
#                                  height='100%',
#                                  width='55%'),
#                         html.Figcaption(['Hierarchical clustering visual of Kaibab Plateau spring water chemistry'
#                                         ]),
#                         ], fluid=True),
#                             ],
#                             width='30%'),

#                     dbc.Col([
#                         html.Img(src="https://lh3.googleusercontent.com/BUJCYRgyFbcsHFW56kELO0i58FoDqRvbsunylVZvZ4TPxIL8pQBDkKbYP5P6EgJjjIJU-J2JZndv0YIpqHkvGSsCxED_QooQHf9mV4RJhSoUn9nRjaJM4mVrLYcz39RrKSM6HjhQVUQ=w2400",
#                                 #  height='100%',
#                                  width='25%'),
#                         # html.Figcaption(["Image from Wood, A.J., 2019, Hydrogeology of the Coconino Aquifer, Kaibab Plateau, Grand Canyon, AZ"
#                         #                 ]),
#                         html.Img(src='https://lh3.googleusercontent.com/zDu2QO6UXSKzkJPwqsHSFjAwJ2dIqwKItR8Dop5Z2A5AWkRD5xCrRDiHcYbScIDyWba96qa3a65A9xDWYaWCao4KfCsfXdhKkTFpj7tyyIxvtdy4jgAm13OT3Mvu3brBHmkjQZrtbZk=w2400',
#                                 #  height='100%',
#                                  width='25%'),
#                         # html.Figcaption(['Plot of first two principal components and loadings.'
#                         #                 ]),
#                         html.Img(src='https://lh3.googleusercontent.com/QXumJxUypNBlqmhrxzGdE0sK3ME0aArkW2r_kdP-B1t0pjqtfQtnpU163EHkbjY0V0vaKkYWGH7SndkPdJ9N53eDfN5s0HvTW-b7BDAoIjFHuyFR6eVcyTSSkS4Bw9hIOmCzjfJwQso=w2400',
#                                 #  height='100%',
#                                  width='25%'),
#                         # html.Figcaption(['Screeplot of cummulative variance'
#                         #                 ]),
#                         html.Img(src='https://lh3.googleusercontent.com/-CDvzPGOr1vJT_oDr3LAVcYTwkvT5RTaiRWEcO4ylKcxq8Q4aQp_YoByr-NkOUn-MuIh0M41ABkpJsauP3Peaj3VLXnXjNe8G8OXYZNvMmracVZ83rL23pvc4zBIUvfN5SFV3u7t-os=w2400',
#                                 #  height='100%',
#                                  width='25%'),
#                         # html.Figcaption([
#                         #                 ]),

#                              ])
#                 ])
#             ])
#         )

# ],
# fluid=True,
# className="py-3"),


# dbc.Card([
# html.Script(src='https://gist.github.com/37b0a41994bb287029eb6dfb3b88e127.git',
#            style={'width':'100%', 'height': '75vw'}
#    )

# ])
# ]
