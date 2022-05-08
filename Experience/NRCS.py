#!./.venv/bin/python
# -*- coding: utf-8 -*-

from dash import html
import dash_bootstrap_components as dbc


nrcs = [
    dbc.Card(
        [
            html.H4("Data Scientist and Hydrologist | USDA Natural Resources Conservation Service"),
            html.P(
                [
                    html.H5("Portland, OR"),
                    html.H5("October 2020 - Present"),
                ]
            ),
            html.P(
                [
                    html.Ul(
                        [
                            html.Li(
                                [
                                    "Co-author of the monthly ",
                                    html.A(
                                        "Water Supply Outlook Report",
                                        href="https://www.nrcs.usda.gov/wps/portal/nrcs/detail/or/snow/?cid=nrcseprd1721654",
                                        target="_blank",
                                    ),
                                    " for the state of Oregon.",
                                ]
                            ),
                            html.Ul(
                                [
                                    html.Li(
                                        "Initially maintained and ran VBA scripts that partially automated "
                                        "a legacy process."
                                    ),
                                    html.Li(
                                        [
                                            "Built new ",
                                            html.A(
                                                "web app ",
                                                href="https://github.com/geoskimoto/wsor-automated-reporting-demo-version",
                                                target="_blank",
                                            ),
                                            "replacing this legacy process that can now produce reports "
                                            "instantaneously saving hundreds of hours of staff time throughout the "
                                            "year, incorporates new and more flexible technologies, provides a more "
                                            "effective presentation of the information, and whose code base is now "
                                            "cleaner and simpler to maintain.",
                                        ]
                                    ),
                                    # html.Li(
                                    #     'The new system is built around an api that queries and retrieves data '
                                    #     'from the USDA Air-Water and Snow Telemetry Databases and is built '
                                    #     'using Flask and jinja templating.'
                                    # )
                                ]
                            ),
                            html.Li(
                                [
                                    "Project lead for a large data review of all snow telemetry (SNOTEL) datasets "
                                    "within the states of OR and WA with the purpose of updating the region’s "
                                    "precipitation and snow water equivalent ",
                                    html.A(
                                        "30yr central tendency statistics.",
                                        href="https://www.nrcs.usda.gov/wps/portal/wcc/home/snowClimateMonitoring/30YearNormals/",
                                        target="_blank",
                                    ),
                                ]
                            ),
                            html.Ul(
                                [
                                    html.Li(
                                        "Discovered hundreds of errors adversely affecting central tendency "
                                        "statistics through numerous anomaly detection tests (logical, "
                                        "statistical/machine learning, visual, and regression) and evaluated stations "
                                        "for changes in data collection after major disturbance events "
                                        "(e.g. fires, logging)."
                                    )
                                ]
                            ),
                            html.Li(
                                [
                                    "Built regression web app (see Coding Portfolio tab) to quickly estimate null or "
                                    "erroneous data saving hours of staff time every week and providing a more "
                                    "consistent, accurate, and defensible means of estimating data compared to previous"
                                    " methods."
                                ]
                            ),
                            html.Li(
                                "Actively review daily data from all WA SNOTEL stations looking for anomalies.  "
                                "Additionally, creating a passive notification system and dashboard to "
                                "automatically alert reviewers when anomalies are detected."
                            ),
                            html.Li(
                                [
                                    "Maintain and repair over 180 ",
                                    html.A(
                                        "SNOTEL weather stations ",
                                        href="https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap#version=158&elements=&networks=!&states=!&counties=!&hucs=&minElevation=&maxElevation=&elementSelectType=any&activeOnly=true&activeForecastPointsOnly=false&hucLabels=false&hucIdLabels=false&hucParameterLabels=true&stationLabels=&overlays=&hucOverlays=2&basinOpacity=75&basinNoDataOpacity=25&basemapOpacity=100&maskOpacity=0&mode=data&openSections=dataElement,parameter,date,basin,options,elements,location,networks&controlsOpen=true&popup=&popupMulti=&popupBasin=&base=esriNgwm&displayType=station&basinType=6&dataElement=WTEQ&depth=-8&parameter=PCTMED&frequency=DAILY&duration=I&customDuration=&dayPart=E&year=2022&month=4&day=18&monthPart=E&forecastPubMonth=4&forecastPubDay=1&forecastExceedance=50&seqColor=1&divColor=7&scaleType=D&scaleMin=&scaleMax=&referencePeriodType=POR&referenceBegin=1991&referenceEnd=2020&minimumYears=20&hucAssociations=true&lat=43.493&lon=-115.873&zoom=6.0",
                                        target="_blank",
                                    ),
                                    "throughout OR and WA.",
                                    html.Ul(
                                        [
                                            html.Li(
                                                "Field work requires significant electronic (sensors and loggers) "
                                                "skills, and moderate electrician (solar power and battery banks) "
                                                "and carpentry skills (power saws, framing, basic foundation work)."
                                            ),
                                            html.Li(
                                                "Additionally sites are often in rugged terrain requiring several modes"
                                                " of transportation to gain access including pickup trucks,"
                                                " helicopters, utvs, horseback, backcountry skis, snowmobiles, and/or"
                                                " snowcats."
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    )
                ]
            ),
        ],
        className="card mb-4 border-0",
    )
]
