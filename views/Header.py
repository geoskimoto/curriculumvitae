import dash_bootstrap_components as dbc
from dash import html
from flask import url_for

header = dbc.Card(
    [
        # dbc.CardImg(src='', top=True),
        dbc.CardBody(
            [
                html.P(
                    [
                        html.H4(
                            ["Nicholas Steele | Data Scientist & Hydrogeologist"],
                            # className="card-title",
                            # style={
                            #     'align': 'center'
                            # }
                        ),
                        html.P(
                            [
                                "Applying data science solutions to meteorology, surface hydrology, and groundwater "
                                "challenges."
                            ],
                            # className="card-text",
                            # style={
                            #     'align': 'center'
                            # }
                        ),
                    ],
                    # style={
                    #
                    # }
                ),
                # html.Img(url_for('assets', filename='Screenshot 2022-04-13 165710.png'),
                #          width='250',
                #          height='300'),
                # html.Img(src='https://i.ibb.co/gSXVzsB/20181006-140457.jpg',
                #         width="400",
                #         height = "500"
                #         )
            ],
        ),
        # html.Hr(
        #    style={'height': '1px',
        #            'width':'100%',
        #            'background':'teal',
        #            # 'margin': '15px',
        #            # 'align':'center'
        #            # 'margin-left': '10%',
        #            # 'margin-right':'10%'
        #     }
        # ),
    ],
    className="card mb-4 border-0",
    # style={
    #     'align-items': 'center',
    #     'justify-content': 'left'
    # }
)
