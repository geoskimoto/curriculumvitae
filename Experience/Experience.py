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
                                    'Project lead for a large data review of all datasets within the jurisdiction of the OR Data Collection Office (ORDCO).'
                                        ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                'Discovered hundreds of errors adversely affecting central tendency statistics through numerous anomaly ' 
                                                'detection tests (logical tests, statistical tests, visual tests, and regression) and evaluated stations for changes '
                                                'in data collection after major disturbance events (e.g. fires, logging).'
                                            )
                                        ]
                                    ),
                                html.Li(
                                    'Built regression web app tool to quickly estimate missing or bad data saving hundreds of hours of staff time and providing '
                                    'a more consistent, accurate, and defensible means at estimating data than previous methods.'
                                ),
                                html.Li(
                                    'Actively review daily data from all WA SNOTEL stations looking for sensor errors/failures.  Additionally, creating a passive '
                                    'notification system and dashboard to automatically alert editors to anomalies.'
                                ),
                                html.Li([
                                    'Maintain and repair ',
                                    html.A(
                                        'SNOTEL weather stations throughout OR and WA.',
                                        href='https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap#version=158&elements=&networks=!&states=!&counties=!&hucs=&minElevation=&maxElevation=&elementSelectType=any&activeOnly=true&activeForecastPointsOnly=false&hucLabels=false&hucIdLabels=false&hucParameterLabels=true&stationLabels=&overlays=&hucOverlays=2&basinOpacity=75&basinNoDataOpacity=25&basemapOpacity=100&maskOpacity=0&mode=data&openSections=dataElement,parameter,date,basin,options,elements,location,networks&controlsOpen=true&popup=&popupMulti=&popupBasin=&base=esriNgwm&displayType=station&basinType=6&dataElement=WTEQ&depth=-8&parameter=PCTMED&frequency=DAILY&duration=I&customDuration=&dayPart=E&year=2022&month=4&day=18&monthPart=E&forecastPubMonth=4&forecastPubDay=1&forecastExceedance=50&seqColor=1&divColor=7&scaleType=D&scaleMin=&scaleMax=&referencePeriodType=POR&referenceBegin=1991&referenceEnd=2020&minimumYears=20&hucAssociations=true&lat=43.493&lon=-115.873&zoom=6.0'
                                        )
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
                                                'Maintain and run Visual Basics for Applications scripts to produce reports. Currently rewriting and upgrading '
                                                'report to include better technologies and increase efficiency.'
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




#
# ●
# ○
# ●
# ●
# ●
# ●
# ○
