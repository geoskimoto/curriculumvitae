from dash import html
import dash_bootstrap_components as dbc
from maindash import app
from dash.dependencies import Input, Output
from Portfolio.SNOTELRegression import snotel_regr_tool
from Portfolio.KP_WaterChem import kp_waterchem

projects = [
    {"label": "SNOTEL Regression Tool", "value": "snotel-regression-tool"},
    {"label": "SNOTEL Anomaly Detection", "value": "snotel-anomaly_detection"},
    {"label": "SNOTEL Change Detection", "value": "snotel-change-detection"},
    {"label": "Phantom Ranch, Grand Canyon Groundwater Model", "value": "pr-gndwater-model"},
    {"label": "Kaibab Plateau Spring PCA and Clustering Analysis", "value": "kaibab-pca"},
    {"label": "Roaring Springs Precipitation Response Analysis", "value": "rs-precip-response"},
    {"label": "This website", "value": "CV"},
    {"label": "Collection of smaller projects", "value": "small-projects"}
]
#
projects_dropdown = html.Div(id='proj-selector-Div',
             children=[
                 dbc.Select(
                     id='project-selector',
                     options=projects,
                     value='snotel-regression-tool'
                 )
                 ]
                         )

@app.callback(Output('projects-div', 'children'),
              Input('project-selector', 'value'),
              # prevent_initial_call=True
              )

def Projects(project_selection):
    
    if project_selection == "snotel-regression-tool":
        return snotel_regr_tool
    if project_selection == "kaibab-pca":
        return kp_waterchem
    else:
        pass
    
    
#     a = RoseScatterPlot(skill_selection)
#     a.rose_scatter_plot()
#
#
#     RosePlot = (
#             html.Div(
#                 children=[
#                     dcc.Graph(
#                         figure=a.rose_plot,
#                         # responsive=True,
#                     )
#                 ]
#             ),
#     )
#
#     return RosePlot