from dash import html
import dash_bootstrap_components as dbc

seismo_lab = [
    dbc.Card(
        [
            html.H4("Research Assistant and Lab Tech | NV Seismology Laboratory"),
            html.P(
                [
                    html.H5("Reno, NV"),
                    html.H5("September 2006 - May 2010"),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                "Research assistant participating in two different exploration research projects "
                                "as a student under Professor Ileana Tribuleac."
                            ),
                            html.Li(
                                "Used new ambient source techniques(e.g. seismic waves created from weather, "
                                "oceanic waves and motor-traffic) in order to locate subsurface features such as "
                                "faults and large stratigraphic differentiations.  Purpose was to produce a cost "
                                "effective passive technique (vs. active techniques using explosives, hammers, and "
                                "earthquakes) to delineate subsurface stratigraphy and structures."
                            ),
                            html.Li(
                                "Located and determined properties of earthquakes from national networks of "
                                "seismographs.  "
                            ),
                        ]
                    )
                ]
            ),
        ],
        className="card mb-4 border-0",
    )
]
