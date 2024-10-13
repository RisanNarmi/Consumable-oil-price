from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
app.title = "Consumable Oil Price"
server = app.server

#read processes-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/Consumable-oil-price/refs/heads/main/Assets/8%20Edible%20Oils.csv")

#style set------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#606e87",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Consumable Oil Data", className="display-4"),
        html.Hr(),
        html.P(
            "Consumtion & price of the 8 main consumable oils by year by per metric tonnes", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Welcome Page", href="/", active="exact"),
                dbc.NavLink("Consumption Data", href="/page-1", active="exact"),
                dbc.NavLink("Price Data", href="/page-2", active="exact"),
                dbc.NavLink("Unit price", href="/page-3", active="exact"),
                dbc.NavLink("Analysis", href="/page-4", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

#Site Layout--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

#callback-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#graph framework----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#error test---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
