import os
import dash_bootstrap_components as dbc
from dash import html

email = os.getenv('email')
phone_number = os.getenv('phone-number')

contact = [
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Img(
                                                                src="https://lh3.googleusercontent.com/oKuGmUfxaN6si1zbFs1nsTNh_dzuQ7kM1Wems22vHKrk-LkO99RQofB_pbw3opt1FeN2-IiuqPmRq6x8w0WOkwV6H7NJdC5ifPyxXygb-TtnP650NOw-_H6qweYjdmkXswH0tL8CMEg=w2400",
                                                                height="30px",
                                                                width="30px",
                                                            ),
                                                        ],
                                                        style={
                                                            "display": "inline-block",
                                                            "vertical-align": "top",
                                                        },
                                                    ),
                                                ],
                                                width=2,
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [
                                                            html.H6(
                                                                [
                                                                    html.A(
                                                                        email,
                                                                        href=f"mailto: {email}",
                                                                    )
                                                                ]
                                                            )
                                                        ],
                                                        style={
                                                            "height": "115%",
                                                            "width": "100%",
                                                            "display": "flex",
                                                            "align-items": "center",
                                                            "justify-content": "left",
                                                        },
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                ]
                            ),
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Img(
                                                                src="https://lh3.googleusercontent.com/ZxAQ4FbVECc45MbY6reQda_8XxDOq9YaDST9weKqP_GsHHRsDeLDAhQKat3Fa1G1K1AYHps0w0beqPmgvmjVgqVDj7iS9XMXIHOWjR_FxflSOzFnl-b6xTx1IeFN2laZfe0S-_c7580=s128-p-k",
                                                                height="25px",
                                                                width="25px",
                                                            ),
                                                        ]
                                                    ),
                                                ],
                                                width=2,
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [html.H6(f"{phone_number}")],
                                                        style={
                                                            "height": "115%",
                                                            "width": "100%",
                                                            "display": "flex",
                                                            "align-items": "center",
                                                            "justify-content": "left",
                                                        },
                                                    )
                                                ]
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [
                                                            html.A(
                                                                href="https://www.linkedin.com/in/nicholas-s-53183617/",
                                                                children=[
                                                                    html.Img(
                                                                        src="https://lh3.googleusercontent.com/niF5L1sLPogflQ81E74CkWozw1AQWva67aMtUUvqBFRPbzE56gieLR4Rjno2madt_tQmxe4tuEFw7XQ8h-jHiiVO0cikdXWcC22itzYqBXW96-8ZtW0AMoOJwZXL2xdsgJQpJDXrF2M=s16-p-k",
                                                                        height="25px",
                                                                        width="25px",
                                                                    )
                                                                ],
                                                            ),
                                                        ]
                                                    )
                                                ],
                                                width=2,
                                            ),
                                            # dbc.Col(
                                            #     [
                                            #         html.Div(
                                            #             [
                                            #                 html.H6(['linkedin.com/in/nicholas-s-53183617'],
                                            #                         style=
                                            #                             {
                                            #                             'font-size':'12px'
                                            #                             }
                                            #                         )
                                            #             ],
                                            #             style={
                                            #                 'height': '115%',
                                            #                 'width': '100%',
                                            #                 'display': 'flex',
                                            #                 'align-items': 'center',
                                            #                 'justify-content': 'left'
                                            #             }
                                            #         )
                                            #     ]
                                            # ),
                                            #             ]
                                            #         )
                                            #     ]
                                            # ),
                                            dbc.Col(
                                                [
                                                    html.A(
                                                        href="https://github.com/geoskimoto",
                                                        children=[
                                                            html.Img(
                                                                src="https://lh3.googleusercontent.com/Hg4oO1xxtkKc5NAQsEap0ExvoBJcBtT0qSYhxQIPh7PLjm7DwcDGf_DC9mq8ANa4A9vOTHEMulU52e_gkdU5NQLBkmawJMpCwLUWRfLsJHHr5muhL0uZUg_xrAa6eyIBnBg5FBiPWaI=s128-p-k",
                                                                height="25px",
                                                                width="25px",
                                                            ),
                                                        ],
                                                    )
                                                ],
                                                width=2,
                                            ),
                                        ]
                                    )
                                ]
                            ),
                        ]
                    ),
                ]
            ),
            #     html.Hr(
            #     style={'height': '1px',
            #            'width': '100%',
            #            'background': 'teal',
            #            # 'margin': '15px',
            #            # 'align': 'center'
            #            'margin-left': '0%',
            #            'margin-right': '0%'
            #         }
            #     ),
        ],
        # className="card mb-4 border-0"
    )
]
