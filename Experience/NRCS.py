#!./.venv/bin/python
# -*- coding: utf-8 -*-

from dash import html
import dash_bootstrap_components as dbc

nrcs = [
    dbc.Card(
        [
            html.H4("Hydrologist | USDA Natural Resources Conservation Service"),
            html.P(
                [
                    html.H5('Portland, OR'),
                    html.H5('October 2020 - Present'),
                ]
            ),
        # dbc.Accordion([
            # dbc.AccordionItem([
                html.P(
                    [
                        html.Ul(
                            [
                                html.Li(
                                    'Project lead for a large data review of all snow telemetry (SNOTEL) datasets within the states of OR and WA in order '
                                    'to update region’s precipitation and snow water equivalent 30yr central tendency statistics.'
                                        ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                'Discovered hundreds of errors adversely affecting central tendency statistics through numerous anomaly ' 
                                                'detection tests (logical, statistical, visual, and regression) and evaluated stations for changes '
                                                'in data collection after major disturbance events (e.g. fires, logging).'
                                            )
                                        ]
                                    ),
                                html.Li(
                                    'Built regression web app tool to quickly estimate null or erroneous data saving significant staff time and providing '
                                    'a more consistent, accurate, and defensible means of estimating data compared to previous methods.'
                                ),
                                html.Li(
                                    'Actively review daily data from all WA SNOTEL stations looking for anomalies.  Additionally, creating a passive '
                                    'notification system and dashboard to automatically alert reviewers.'
                                ),
                                html.Li([
                                    'Maintain and repair ',
                                    html.A(
                                        'SNOTEL weather stations ',
                                        href='https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap#version=158&elements=&networks=!&states=!&counties=!&hucs=&minElevation=&maxElevation=&elementSelectType=any&activeOnly=true&activeForecastPointsOnly=false&hucLabels=false&hucIdLabels=false&hucParameterLabels=true&stationLabels=&overlays=&hucOverlays=2&basinOpacity=75&basinNoDataOpacity=25&basemapOpacity=100&maskOpacity=0&mode=data&openSections=dataElement,parameter,date,basin,options,elements,location,networks&controlsOpen=true&popup=&popupMulti=&popupBasin=&base=esriNgwm&displayType=station&basinType=6&dataElement=WTEQ&depth=-8&parameter=PCTMED&frequency=DAILY&duration=I&customDuration=&dayPart=E&year=2022&month=4&day=18&monthPart=E&forecastPubMonth=4&forecastPubDay=1&forecastExceedance=50&seqColor=1&divColor=7&scaleType=D&scaleMin=&scaleMax=&referencePeriodType=POR&referenceBegin=1991&referenceEnd=2020&minimumYears=20&hucAssociations=true&lat=43.493&lon=-115.873&zoom=6.0',
                                        target='_blank'
                                        ),
                                    'throughout OR and WA.'
                                    ]
                                ),
                                html.Li([
                                    'Assist in authoring monthly ',
                                        html.A('Water Supply Outlook Reports',
                                           href='https://www.nrcs.usda.gov/wps/portal/nrcs/detail/or/snow/?cid=nrcseprd1721654',
                                           target='_blank'
                                           )
                                    ]
                                ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                'Maintained and ran VBA scripts that automated much of the process.'
                                            ),
                                            html.Li(
                                                'Assisted creating new API to automatically serve data and rewrote report using a '
                                                'microservices architecture and based on a markup language format.  Report can now '
                                                'be instantaneously produced, incorporates new technologies like interactive plots '
                                                'and maps, presents the information much more effectively, and the code base is now '
                                                'much cleaner and simpler to maintain.'

                                            )
                                        ]
                                    )
                            ]
                        )
                    ]
                )
        ]
    )
]


# if __name__ == "__main__":
#     print("I do nothing, just non dynamic components that take up space...")
