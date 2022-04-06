
import dash_bootstrap_components as dbc
from Experience.GRCA import grca
from Experience.NRCS import nrcs
from Experience.SkiPatrol import skipatrol
from Experience.TICA import tica
from Experience.Golder import golder
from dash import html

Experience = dbc.Row([
                    dbc.Col(
                        [
                            dbc.Accordion([
                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(nrcs)
                                        )
                                    ],
                                    title='Hydrologist | USDA - NRCS'
                                    # title='October 2020 - Present'
                                ),

                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(grca)
                                        ),
                                    ],
                                    title='Physical Scientist | NPS - Grand Canyon National Park'
                                ),
                                dbc.AccordionItem([
                                    dbc.Row(
                                        dbc.Col(tica)
                                    ),
                                    ],
                                    title='Physical Scientist and EMT | NPS - Timpanogos Cave National Monument'
                                ),
                                dbc.AccordionItem([
                                    dbc.Row(
                                        dbc.Col(skipatrol)
                                    ),
                                    ],
                                    title='Ski Patroller | Vail - Park City Mountain Resort'
                                ),
                                dbc.AccordionItem([
                                    dbc.Row(
                                        dbc.Col(golder)
                                    ),
                                    ],
                                    title='Geologist | Golder Associates'
                                )
                            ]
                            )
                        ]
                    )
    ])











if __name__ == "__main__":
    print('I do nothing but import experience modules into app.py')