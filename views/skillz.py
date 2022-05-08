import plotly.graph_objects as go


class RoseScatterPlot:
    def __init__(self, skill):
        if skill == "DS":
            skillz = {
                "SQL": {
                    "r": 40,
                    "Stack": (
                        "MySQL, sqlite, flask-sqlalchemy, sqlalchemy, Aquarius Time-Series Water SQL Data "
                        "Management Software"
                    ),
                    "Abilities": "CRUD operations, backend database web development",
                },
                "Visualizations": {
                    "r": 60,
                    "Stack": "plotly, seaborn, matplotlib, dash + flask",
                    "Abilities": "Full featured interactive visualizations and dashboard web applications",
                },
                "Machine Learning": {
                    "r": 55,
                    "Stack": "scikit-learn, XGBoost, PySpark (Mllib)",
                    "Abilities": (
                        "Classification and Regression (XGBoost and other tree methods, SVM w/kernel methods, "
                        "lasso & ridge, logistic), Clustering (kmeans+, mixture of gaussians, hierarchical), "
                        "Principal Component Analysis"
                    ),
                },
                "Data Wrangling": {
                    "r": 65,
                    "Stack": "pandas, numpy, excel + vba",
                    "Abilities": "discovery, structuring for analysis, cleaning, QA/QC",
                },
                "Deep Learning": {
                    "r": 40,
                    "Stack": "tensorflow, keras",
                    "Abilities": "CNN, RNN, and LSTM neural networks",
                },
                "NLP": {
                    "r": 35,
                    "Stack": "nltk, regular expressions, textblob, wordcloud, vader, Twitter API",
                    "Abilities": "tokenization, lemmatization, and performing sentiment analysis",
                },
                "Data Scraping": {
                    "r": 45,
                    "Stack": "beautifulsoup, scrapy, requests, Selenium, RESTful and SOAP web services",
                    "Abilities": (
                        "scrape data from html, automate forms to retrieve data, connect web services directly "
                        "to applications"
                    ),
                },
                "Anomaly Detection": {
                    "r": 55,
                    "Stack": "pyod, scikit-learn, statsmodels, hampel",
                    "Abilities": (
                        "IsolationForests, LocalOutlier, and Hampel Filter for non-Guassian distributions, Z-Score,"
                        " regression, logical tests based on domain knowledge, change detection tests (double mass"
                        " analysis)"
                    ),
                },
                "TS Forecasting": {
                    "r": 50,
                    "Stack": "statsmodels, scikit-learn, datetime, tensorflow, fbprophet",
                    "Abilities": "SARIMAX, LSTM, Prophet forecasting models",
                },
            }
            # r_list = [parameter['r'] for parameter in skillz.values() if 'r' in parameter.keys()]
            # stack_list = [parameter['Stack'] for parameter in skillz.values() if 'Stack' in parameter.keys()]
            # abilities_list = [parameter['Abilities'] for parameter in skillz.values() if 'Abilities' in parameter.keys()]

        elif skill == "Other Computer":
            skillz = {
                "Web Dev": {
                    "r": 50,
                    "Stack": "flask, html/css/bootstrap, sqlalchemy, jinja templating, dash, javascript",
                    "Abilities": (
                        "Full featured web apps and REST APIs with session caching, sql database support, and "
                        "authentication."
                    ),
                },
                "Groundwater Modelling": {
                    "r": 50,
                    "Stack": "flopy, geopandas, fiona, rasterio, Modflow, ModelMuse",
                    "Abilities": (
                        "Build, calibrate, and run predictions for finite-difference groundwater models "
                        "solving problems involving pumping/injection, groundwater-surface water "
                        "interactions, evapotranspiration, and/or contaminant transport."
                    ),
                },
                "Big Data": {
                    "r": 45,
                    "Stack": "pyspark (RDD, SQL and DataFrame, MLlib)",
                    "Abilities": (
                        "Statistical and machine learning analysis on very large datasets using distributed systems."
                    ),
                },
                "GIS - Software": {
                    "r": 60,
                    "Stack": "ESRI Products, QGIS",
                    "Abilities": (
                        "Any local to regional scaled raster or vector based analysis using traditional GUI software."
                    ),
                },
                "GIS - Script & Visuals": {
                    "r": 55,
                    "Stack": (
                        "geopandas, pyproj, gdal, fiona, rasterio, Earth Engine API, plotly mapbox, leaflet, "
                        "folium, ESRI products, QGIS"
                    ),
                    "Abilities": (
                        "Any local to globally scaled raster or vector based analysis directly scripted, "
                        "especially related to hydrology applications. Globally scaled analysis is done using "
                        "the Earth Engine APIs. Can automate analysis and integrate results into web "
                        "frameworks. Efficient with geodatabases."
                    ),
                },
            }
            # r_list = [parameter['r'] for parameter in skillz.values() if 'r' in parameter.keys()]
            # stack_list = [parameter['Stack'] for parameter in skillz.values() if 'Stack' in parameter.keys()]
            # abilities_list = [parameter['Abilities'] for parameter in skillz.values() if
            #                   'Abilities' in parameter.keys()]

        elif skill == "Coding":
            skillz = {
                "Python": {
                    "r": 55,
                    # 'Stack': '',
                    # 'Abilities': ''
                },
                "R": {"r": 30},
                "vba": {"r": 25},
                "html, css, & bootstrap": {"r": 55},
                "javascript": {"r": 30},
                "Git": {"r": 45},
                "Data Stux and Algos": {"r": 30},
                "SOLID Principles": {"r": 25},
            }

        r_list = [parameter["r"] for parameter in skillz.values() if "r" in parameter.keys()]
        stack_list = [parameter["Stack"] for parameter in skillz.values() if "Stack" in parameter.keys()]
        abilities_list = [parameter["Abilities"] for parameter in skillz.values() if "Abilities" in parameter.keys()]

        # self.skills = skillz
        self.theta = list(skillz.keys())
        self.r = r_list
        self.stack = stack_list
        self.abilities = abilities_list

    def rose_scatter_plot(self):
        fig = go.Figure(
            data=go.Scatterpolar(
                r=self.r,
                theta=self.theta,
                fill="toself",
                line=dict(color="salmon"),
            )
        )

        fig.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            font=dict(size=14),
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 80],
                    tickvals=[20, 40, 60],
                    ticktext=["Basic", "Intermediate", "Advanced"],
                    tickmode="array",
                    tickangle=25,
                    tickfont=dict(family="Arial", size=14, color="#acb3bf"),
                )
            ),
            showlegend=False,
            # autosize is the key to getting plot to center itself in dcc.graph and divs.  If you specify height and width, it locks it in place as left aligned.
            autosize=True
            # height=450,
            # width=450
        )

        fig.update_traces(hoverinfo="none", hovertemplate=None)
        self.rose_plot = fig


if __name__ == "__main__":
    print("I am the class that creates the roseplot in app.py")
