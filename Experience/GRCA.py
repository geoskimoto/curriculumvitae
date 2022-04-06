#!./.venv/bin/python
# -*- coding: utf-8 -*-

from dash import html
import dash_bootstrap_components as dbc

grca = [
    dbc.Card(
        [
            html.H4("Physical Science Technician | DOI NPS Grand Canyon National Park"),
            html.P(
                [
                    html.H5('Flagstaff, AZ'),
                    html.H5('February 2016 - October 2020'),
                ]
            ),

            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                'Represented the Physical Sciences Program through formal presentations to executive teams and scientific conferences.  '
                                'Provided an active voice in park management concerns and a face for the program. Maintained relationships with other '
                                'agencies, universities, outside researchers, and contractors.'
                            ),
                            html.Li(
                                'Acquired funding and managed a precipitation-response study to characterize the connection between sinkholes on the Kaibab '
                                'Plateau and spring discharge.  Study is being used to inform the replacement of water infrastructure of the park.'
                            ),
                            html.Li(
                                'Field lead for a complex dye tracer study from 2014 - 2017 aimed at better understand vulnerabilities, flow paths, and water '
                                'budgets of Grand Canyon aquifers.  Work has been used in several publications.'
                            ),
                            html.Li(
                                'Created and applied a groundwater model successfully assessing the impact of groundwater withdrawal from proposed wells on '
                                'Bright Angel Creek.   Results were used to inform a NEPA Environmental Assessment.  Project won first place in the 2018 '
                                'Arizona Hydrological Society poster competition.'
                            ),
                            html.Li(
                                'Actively maintained the park’s twelve flow gaging and water quality sites and collected discrete data at other springs and '
                                'creeks within the canyon.'
                            ),
                            html.Li(
                                'Maintained two interagency meteorology and air pollutant monitoring stations.'
                            ),
                            html.Li(
                                'Frequently participated in cave macroinvertebrate, bat, archaeological, and mapping surveys as well as installing acoustic bat '
                                'detectors and environmental sensors.'
                            ),
                            html.Li(
                                'Created a quantifiable methodology to better assess vulnerability and prioritize the protection of caves and fossil resources '
                                'within Grand Canyon National Park. Research resulted in a publication.'
                            ),
                            html.Li(
                                'Conducted statistical analysis for Timpanogos Cave National Monument assessing the effectiveness of newly installed doors on cave '
                                'climate using regression analysis, ANOVA, and Tukey’s range tests.  Presented results at the GSA 2016 conference and authored an '
                                'internal report.'
                            )
                        ]
                    )
                ]
            )
        ]
    )
]







