import dash_bootstrap_components as dbc
from Experience.grca import grca
from Experience.nrcs import nrcs
from Experience.skipatrol import skipatrol
from Experience.tica import tica
from Experience.golder import golder
from Experience.kinross import kinross_exploration, kinross_hydro_intern
from Experience.seismo_lab import seismo_lab
from dash import html

Experience = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [dbc.Row(dbc.Col(nrcs))],
                            title="Data Scientist and Hydrologist | USDA - NRCS"
                            # title='October 2020 - Present'
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(grca)),
                                html.P(
                                    style={"page-break-after": "always", "margin-top": "35px", "margin-bottom": "35px"}
                                ),
                            ],
                            title="Physical Scientist | NPS - Grand Canyon National Park",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(skipatrol)),
                            ],
                            title="Ski Patroller | Vail - Park City Mountain Resort",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(tica)),
                            ],
                            title="Physical Scientist and EMT | NPS - Timpanogos Cave National Monument",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(golder)),
                            ],
                            title="Geologist | Golder Associates",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(kinross_exploration)),
                                html.P(
                                    style={"page-break-after": "always", "margin-top": "35px", "margin-bottom": "35px"}
                                ),
                            ],
                            title="Exploration Geologist Intern | Kinross Gold Corporation",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(kinross_hydro_intern)),
                            ],
                            title="Hydrology Intern | Kinross, Round Mountain Gold",
                        ),
                        dbc.AccordionItem(
                            [
                                dbc.Row(dbc.Col(seismo_lab)),
                            ],
                            title="Research Assistant and Lab Tech | NV Seismology Laboratory",
                        ),
                    ],
                    always_open=True,
                )
            ]
        )
    ]
)


if __name__ == "__main__":
    print("I do nothing but import experience modules into app.py")
