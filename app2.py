from views import Header, Contact
from dash.dependencies import Input, Output
import Index
from maindash import app
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

app.title = "NSteele CV"
server = app.server

app.layout = dbc.Container([
    html.Div(
        [
            dcc.Location(id='url', refresh=False),
            dcc.Link('Experience', href='/'),
            # html.Br(),
            dcc.Link('Portfolio', href='/Portfolio')
        ]
    ),
    html.Div([Header,
              ]),
    html.Div(Contact.Contact),
    html.Br(),
    html.Div(id='page-content', children=[]),
    ]
)



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              )
def display_page(pathname):
    def display_page(pathname):
        if pathname == '/':
            return Index.layout
        elif pathname == '/Portfolio':
            return html.Div([html.H5('Hola')])
        else:
            return Index.layout



if __name__ == '__main__':
    app.run_server(debug=True)


