from views.header import header  # need this import for app.py to reference
from views.skillz import RoseScatterPlot
from dash import html, dcc, callback_context, no_update
from flask import session
import dash_bootstrap_components as dbc
from dbs import app
from dash.dependencies import Input, Output

app.server.secret_key = "super secret key"
app.server.config["SESSION_TYPE"] = "filesystem"

skills_buttons = html.Div(
    [
        dbc.ButtonGroup(
            [
                dbc.Button(
                    id="btn-nclicks-1",
                    children="Data Science",
                    n_clicks=0,
                    n_clicks_timestamp=-1,
                    # style=dict(display='block', height='60px', width='200px'),
                    outline=True,
                    size="sm",
                    color="info",
                    className="btn",
                ),
                dbc.Button(
                    id="btn-nclicks-2",
                    children="Other Computer",
                    n_clicks=0,
                    n_clicks_timestamp=-1,
                    # style=dict(display='block', height='60px', width='200px'),
                    outline=True,
                    size="sm",
                    color="info",
                    className="btn",
                ),
                dbc.Button(
                    id="btn-nclicks-3",
                    children="Coding",
                    n_clicks=0,
                    n_clicks_timestamp=-1,
                    # style=dict(display='block', height='60px', width='200px'),
                    outline=True,
                    size="sm",
                    color="info",
                    className="btn",
                ),
                # dbc.Button(id='project-management-skills',
                #             children='Project Management Skills',
                #             n_clicks=0,
                #             n_clicks_timestamp=-1,
                #            style=dict(display='block', height='60px', width='200px'),
                #            className='btn'),
                # dbc.Button(id='btn-nclicks-4',
                #            children='Hydrogeology',
                #            n_clicks=0,
                #            n_clicks_timestamp=-1,
                #            # style=dict(display='block', height='60px', width='200px'),
                #            outline=True,
                #            size='sm',
                #            color="info",
                #            className='btn'),
                # dbc.Button(id='btn-nclicks-5',
                #            children='EMS',
                #            n_clicks=0,
                #            n_clicks_timestamp=-1,
                #            # style=dict(display='block', height='60px',
                #            #            width='200px'),
                #            outline=True,
                #            size='sm',
                #            color="info",
                #            className='btn'),
                # dbc.Button(id='btn-nclicks-6',
                #            children='Remote Site Access',
                #            n_clicks=0,
                #            n_clicks_timestamp=-1,
                #            # style=dict(display='block', height='60px',
                #            #            width='200px'),
                #            outline=True,
                #            size='sm',
                #            color="info",
                #            className='btn')
            ],
            vertical=False,
            size="lg",
        ),
    ],
    style={"text-align": "center"},
)


@app.callback(
    Output("rose-fig", "children"),
    Input("btn-nclicks-1", "n_clicks"),
    Input("btn-nclicks-2", "n_clicks"),
    Input("btn-nclicks-3", "n_clicks"),
    # Input('btn-nclicks-4', 'n_clicks'),
    # Input('btn-nclicks-5', 'n_clicks'),
    # Input('btn-nclicks-6', 'n_clicks')
)
def update_skills(btn_1, btn_2, btn_3):
    #    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    changed_id = callback_context.triggered[0]["prop_id"].split(".")[0]
    if "btn-nclicks-1" in changed_id:
        skill_selection = "DS"
    elif "btn-nclicks-2" in changed_id:
        skill_selection = "Other Computer"
    elif "btn-nclicks-3" in changed_id:
        skill_selection = "Coding"
    # elif 'btn-nclicks-4' in changed_id:
    #     skill_selection = 'Hydrogeology'
    # elif 'btn-nclicks-5' in changed_id:
    #     skill_selection = 'EMS'
    # elif 'btn-nclicks-6' in changed_id:
    #     skill_selection = 'Remote Site Access'
    else:
        skill_selection = "DS"

        # use this for troubleshooting. Comment out above line and uncomment this block.
        # ctx_msg = json.dumps({
        #    'states': callback_context.states,
        #    'triggered': callback_context.triggered,
        #    'inputs': callback_context.inputs
        # }, indent=2)
        # return html.Div([html.Pre(ctx_msg),
        #                 html.Pre(changed_id)])

    session["skill_selection"] = skill_selection
    plot = RoseScatterPlot(skill_selection)
    plot.rose_scatter_plot()
    RosePlot = (
        dcc.Graph(
            id="graph-basic-2",
            figure=plot.rose_plot,
            clear_on_unhover=True,
            # responsive=True,
            # fluid=True
            style={
                "width": "115%",
                "height": "115%",
                # "margin": "auto",
                # "display": "inline-block",
                # 'textAlign': "center",
                # "border": "3px #5c5c5c dashed",
                # "overflow": "hidden",
                "padding-top": "-100px",
                # "padding-bottom": "-100px",
                # "padding-left": "-100px",
                # "padding-right": "-100px",
                # 'margin-left': '25px',
                # 'margin-right': '-50px'
            },
        ),
        dcc.Tooltip(id="graph-tooltip"),
    )

    return RosePlot


@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph-basic-2", "hoverData"),
)
def display_hover(hoverData):

    if hoverData is None:
        return False, no_update, no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]

    skill_selection = session["skill_selection"]
    plot = RoseScatterPlot(skill_selection)
    theta = plot.theta[num]
    stack = plot.stack[num]
    abilities = plot.abilities[num]

    # print(theta)
    # print(pt)
    # print(bbox)
    # print(num)

    children = [
        html.Div(
            [
                # html.Img(src=img_src, style={"width": "100%"}),
                html.H3(f"{theta}", style={"color": "darkblue"}),
                html.P(f"Stack: {stack}"),
                html.P(f"Abilities: {abilities}"),
            ],
            style={
                "width": "200px",
                "white-space": "normal",
            },
        )
    ]

    return True, bbox, children


if __name__ == "__main__":
    print("I do nothing but import modules into app.py")
