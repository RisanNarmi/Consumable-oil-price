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
                html.H1('Landing Page',
                        style={'textAlign':'center'}),
                dbc.Row([
dbc.Col(html.H1('This is a data visualization assignment for MCM7183 class', className="p-2 bg-light border text-center"))])
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Consumtion by year',
                        style={'textAlign':'center'}),
dbc.Row(dbc.Col(dcc.Slider(2013, 2021, 1, value=2020, id='slider-year',
                         marks = {i: str(i) for i in range(2013, 2022, 1)}, className="mt-5"), width={"size": 10, "offset": 1})), 
dbc.Row(dcc.Graph(id="graph-pie"))
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
    Output('graph-pie', 'figure'),
    Input('slider-year', 'value')
)
def update_graph2(year_selected):
    subYear = df[df['Year'].isin([year_selected])]
    subYear_Coco = subYear['Coconut Oil Consumption(mil tonnes)']
    subYear_Oli = subYear['Olive Oil Consumption(mil tonnes)']
    subYear_PalmK = subYear['Palm Kernel Oil Consumption(mil tonnes)']
    subYear_Palm = subYear['Palm Oil Consumption(mil tonnes)']
    subYear_Nut = subYear['Peanut Oil Consumption(mil tonnes)']
    subYear_Rapeseed = subYear['Rapeseed Oil Consumption(mil tonnes)']
    subYear_Soy = subYear['Soybean Oil Consumption(mil tonnes)']
    subYear_sun = subYear['Sunflower Oil Consumption(mil tonnes)']
    pie_data = [subYear_Coco,subYear_Oli,subYear_PalmK,subYear_Palm,subYear_Nut,subYear_Rapeseed,subYear_Soy,subYear_sun];
    mylabels = ["Coconut Oil", "Olive Oil", "Palm Kernel Oil", "Palm Oil", "Peanut Oil", "Rapeseed Oil", "Soybean Oil", "Sunflower Seed Oil"]
    pie_df = {'Oil Type': mylabels, 'Consumption(Mil. tonnes)': pie_data}
    fig2 = px.pie(pie_df,values="Consumption(Mil. tonnes)",names="Oil Type")
    fig2.update_traces(sort=False) 
    return fig2;

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
