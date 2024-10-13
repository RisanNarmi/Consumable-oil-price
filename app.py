from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
app.title = "Consumable Oil Price"
server = app.server

#read processes-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/Consumable-oil-price/refs/heads/main/Assets/8%20Edible%20Oils.csv")

year = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
Sub2013 = df[df["Year"].isin([2013])]
Sub2014 = df[df["Year"].isin([2014])]
Sub2015 = df[df["Year"].isin([2015])]
Sub2016 = df[df["Year"].isin([2016])]
Sub2017 = df[df["Year"].isin([2017])]
Sub2018 = df[df["Year"].isin([2018])]
Sub2019 = df[df["Year"].isin([2019])]
Sub2020 = df[df["Year"].isin([2020])]
Sub2021 = df[df["Year"].isin([2021])]

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
        html.H2("Edible Oil Data", className="display-4"),
        html.Hr(),
        html.P(
            "Consumtion & price of the 8 main consumable oils by year", className="lead"
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
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Home Page',
                        style={'textAlign':'center'}),
                dbc.Row([
dbc.Col(html.H1('MCM7183 Exercise 3', className="p-2 bg-light border text-center"),  width=10), 
dbc.Col(html.Img(src=image_path, className="m-2"))])
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Edible Oil Global Consumtion',
                        style={'textAlign':'center'}),
dbc.Row(html.h3('consumtion in million tonnes')),
dbc.Row(fig = go.Figure(data=[
    go.Bar(name='Coconut Oil', x=year, y=df["Coconut Oil Consumption(mil tonnes)"]),
    go.Bar(name='Olive Oil', x=year, y=df["Olive Oil Consumption(mil tonnes)"]),
    go.Bar(name='Palm Kernel Oil', x=year, y=df["Palm Kernel Oil Consumption(mil tonnes)"]),
    go.Bar(name='Palm Oil', x=year, y=df["Palm Oil Consumption(mil tonnes)"]),
    go.Bar(name='Peanut Oil', x=year, y=df["Peanut Oil Consumption(mil tonnes)"]),
    go.Bar(name='Papeseed Oil', x=year, y=df["Rapeseed Oil Consumption(mil tonnes)"]),
    go.Bar(name='Soybean Oil', x=year, y=df["Soybean Oil Consumption(mil tonnes)"]),
    go.Bar(name='Sunflower Oil', x=year, y=df["Sunflower Oil Consumption(mil tonnes)"])
]))
                ]
    elif pathname == "/page-2":
        return [
                html.H1('Yearly GDP',
                        style={'textAlign':'center'}),
dbc.Row(dbc.Col(dcc.Checklist(
                    id="checklist",
                    options=["Coconut Oil Price", "Olive Oil Price", "Palm Kernel Oil Price", "Palm Oil Price", "Peanut Oil Price", "Rapeseed Oil Price", "Soybean Oil Price", "Sunflower Oil Price",],
                    value=["Palm Oil Price"],
                    inline=True
                ))), 
dbc.Row(dcc.Graph(id="line-graph"))
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Container(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


#graph framework----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.callback(
    Output("line-graph", "figure"), 
    Input("checklist", "value"))

def update_graph2(type):
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    for type in type:
        trace = go.Scatter(x=df["Month"], y=df[checklist], name=checklist)
        fig.add_trace(trace)
    return fig2;


#error test---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
