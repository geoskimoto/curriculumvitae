from dash import html
import dash_bootstrap_components as dbc
from dbs import app
from dash.dependencies import Input, Output
from Portfolio.regression_tool import snotel_regr_tool
from Portfolio.kp_waterchem import kp_waterchem
from Portfolio.wsor import wsor
from Portfolio.other_projects import other_projects

projects = [
    {"label": "SNOTEL Regression Tool", "value": "snotel-regression-tool"},
    # {"label": "SNOTEL Anomaly Detection", "value": "snotel-anomaly_detection"},
    {"label": "Automated Water Supply Outlook Report", "value": "wsor"},
    # {"label": "SNOTEL Change Detection", "value": "snotel-change-detection"},
    # {"label": "Phantom Ranch, Grand Canyon Groundwater Model", "value": "pr-gndwater-model"},
    {
        "label": "Kaibab Plateau Spring PCA and Clustering Analysis",
        "value": "kaibab-pca",
    },
    # {"label": "Roaring Springs Precipitation Response Analysis", "value": "rs-precip-response"},
    # {"label": "This website", "value": "CV"},
    # {"label": "Collection of smaller projects", "value": "small-projects"}
    {"label": "Other Projects", "value": "other-projects"},
]
#
projects_dropdown = html.Div(
    id="proj-selector-Div",
    children=[
        dbc.Select(
            id="project-selector", options=projects, value="snotel-regression-tool"
        )
    ],
    style={"width": "50%", "margin": "auto"},
)


@app.callback(
    Output("projects-div", "children"),
    Input("project-selector", "value"),
    # prevent_initial_call=True
)
def Projects(project_selection):

    if project_selection == "snotel-regression-tool":
        return snotel_regr_tool
    if project_selection == "kaibab-pca":
        return kp_waterchem
    if project_selection == "wsor":
        return wsor
    if project_selection == "other-projects":
        return other_projects
    else:
        pass
