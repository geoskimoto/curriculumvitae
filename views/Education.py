from dash import html


education = html.Div(
    [
        html.H4("Education", style={"margin": "25px", "text-align": "center"}),
        # html.Hr(
        #     style={'height': '1px',
        #            'background': 'teal',
        #            'margin': '15px 0px 15px'
        #            }
        # ),
        html.P(
            [
                html.H5("Hydrogeology - B.Sc. Honors"),
                html.H6(
                    "University of Nevada, Reno, 2006-2011",
                    style={"text-align": "center"},
                ),
                html.Hr(
                    style={
                        "height": "2px",
                        "width": "20%",
                        "background": "teal",
                        # 'margin': '15px',
                        # 'align':'center'
                        "margin-left": "40%",
                        "margin-right": "40%",
                    }
                ),
                html.H5("Data Science - Graduate Certificate"),
                html.H6(
                    "University of California, San Diego, 2021",
                    style={"text-align": "center"},
                ),
            ]
        ),
    ]
)
