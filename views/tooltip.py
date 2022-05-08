from dash import Dash, dcc, html, Input, Output, no_update

# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html
# from dash import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd

skillz = [

    ['Data Wrangling', 'Visualizations', 'Machine Learning', 'Deep Learning', 'SQL', 'NLP',
     'Data Scraping', 'TS Forecasting', 'Anomaly Detection'
     ],
    [70, 65, 60, 50, 65, 45, 45, 55, 65],
    [
        ['pandas', 'numpy', 'excel/vba'],
        ['plotly', 'seaborn', 'matplotlib', 'dash + flask'],
        ['scikit-learn', 'XGBoost', 'PySpark (Mllib)'],
        ['tensorflow', 'keras'],
        ['MySQL', 'sqlite', 'flask-sqlalchemy', 'sqlalchemy',
         'Aquarius Time-Series Water SQL Data Management Software'],
        ['nltk', 'regular expressions', 'textblob', 'wordcloud', 'vader'],
        ['beautifulsoup', 'requests', 'Selenium', 'RESTful and SOAP web services'],
        ['statsmodels', 'scikit-learn', 'datetime', 'tensorflow', 'fbprophet'],
        ['pyod', 'scikit-learn', 'statsmodels', 'hampel']
    ],
    [
        ['discovery', 'structuring for analysis', 'cleaning', 'QA/QC'],
        ['Full featured interactive visualizations and dashboard web applications'],
        ['Classification and Regression (XGBoost and other tree methods, SVM w/non-linear classifer/regressor,'
         'lasso/ridge, logistic), Clustering (kmeans+, mixture of Gaussians, Heirarichal), Principal Component Analysis'],
        ['CNN, RNN, and LSTM neural networks'],
        ['CRUD operations', 'backend database web development'],
        ['tokenization, lemmatization, and performing sentiment analysis'],
        ['scrape data from html docs, automate forms to retrieve data, connect web services directly to applications'],
        ['SARIMAX, LSTM, Prophet forecasting models'],
        ['IsolationForests, LocalOutlier, and Hampel Filter for non-Guassian distributions'
         'Z-Score, regression, logical tests based on domain knowledge, change detection tests (double mass analysis)']
    ],

    # 'theta':[0,30,60,90,120,150,180,210,240]
]

skillz_df = pd.DataFrame(skillz)
skillz_df.columns = skillz_df.iloc[0, :]
skillz_df.drop([0], inplace=True)

fig = go.Figure(data=go.Scatterpolar(
    r=skillz_df.iloc[0, :],
    theta=skillz_df.columns,
    fill='toself',
    line=dict(color='salmon'),
    # hoverinfo='none',
    # name='',
    # customdata = df,
    # hovertemplate = f'<b>{df}</b>'
))

fig.update_layout(xaxis=dict(visible=False),
                  yaxis=dict(visible=False),
                  font=dict(size=14),
                  polar=dict(
                      radialaxis=dict(
                          visible=True,
                          range=[0, 80],
                          tickvals=[20, 40, 60],
                          ticktext=['Basic', 'Intermediate', 'Advanced'],
                          tickmode='array',
                          tickangle=25,
                          tickfont=dict(
                              family='Arial',
                              size=13,
                              color='#acb3bf'
                          )
                      )
                  ),
                  showlegend=False,
                  height=700,
                  width=700
                  )

# fig = go.Figure(data=[
#     go.Scatter(
#         x=df["LOGP"],
#         y=df["PKA"],
#         mode="markers",
#         marker=dict(
#             colorscale='viridis',
#             color=df["MW"],
#             size=df["MW"],
#             colorbar={"title": "Molecular<br>Weight"},
#             line={"color": "#444"},
#             reversescale=True,
#             sizeref=45,
#             sizemode="diameter",
#             opacity=0.8,
#         )
#     )
# ])

# turn off native plotly.js hover effects - make sure to use
# hoverinfo="none" rather than "skip" which also halts events.
fig.update_traces(hoverinfo="none", hovertemplate=None))

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph-basic-2", figure=fig, clear_on_unhover=True),
    dcc.Tooltip(id="graph-tooltip"),
])


@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph-basic-2", "hoverData"),
)
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]

    skill = skillz_df.columns[num]
    stack = skillz_df.iloc[1, num]
    abilities = skillz_df.iloc[2, num]
    seperator = ", "

    children = [
        html.Div([
            # html.Img(src=img_src, style={"width": "100%"}),
            html.H2(f"{skill}", style={"color": "darkblue"}),
            html.P(f"Stack: {seperator.join(stack)}"),
            html.P(f"Abilitities: {seperator.join(abilities)}"),
        ], style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True)