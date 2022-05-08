#since @app.callbacks in separate files than app.py, placing app here prevents circular imports
import os
from pathlib import Path
from dash import Dash
import dash_bootstrap_components as dbc
from flask_session import Session

from auth import basic_auth

USE_AUTH = os.getenv("USE_AUTH")
AUTH_USER = os.getenv("AUTH_USER")#, "user")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")#, "snotel")


def create_app(use_auth=USE_AUTH):
    # assets_path = Path(APP_DIR, 'assets')
    # https://dash.plotly.com/dash-enterprise/static-assets
    app = Dash(
        __name__,
        # favorites: ZEPHYR, FLATLY, LITERA, LUMEN, QUARTZ, SANDSTONE, SLATE, YETI
        external_stylesheets=[dbc.themes.FLATLY],
        suppress_callback_exceptions=True
    )
    # print(USE_AUTH)
    if use_auth:
        basic_auth.BasicAuth(app, {AUTH_USER: AUTH_PASSWORD})
    Session(app)
    return app


app = create_app()


