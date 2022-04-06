#since @app.callbacks in separate files than app.py, placing app here prevents circular imports

from dash import Dash
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets = [dbc.themes.UNITED])#, suppress_callback_exceptions=True)
