import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table, callback, Input, Output
import mysql.connector

# Conexión a la base de datos MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="PremierLeague"
)

# Consulta SQL para obtener los datos
sql_query = "SELECT * FROM posiciones"
data = pd.read_sql(sql_query, con=db_connection)

# Cerrar la conexión a la base de datos
db_connection.close()

def dashboard(data):
    data_resumen = data.groupby("equipo", as_index=False).sum(numeric_only=True)

    # Diseño utilizando componentes de Dash Bootstrap
    pagina = dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Dashboard Premier League"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.P("Objetivo: Mostrar las estadisticas historicas de todos los equipos que han jugado la Premier League"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.Hr(), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(options=[
                    {"label": "Puntos (PTS)", "value": "pts"},
                    {"label": "Goles a Favor (GF)", "value": "gf"},
                    {"label": "Goles en Contra (GC)", "value": "gc"},
                    {"label": "Diferencia de Goles (DF)", "value": "df"},
                    {"label": "Mostrar Todo", "value": "all"}
                ], value="all", id="dpPremier"),
                width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                    data=data_resumen.drop(columns=['id']).to_dict("records"),
                    page_size=15,
                    id="tblPremier",
                    style_table={'overflowX': 'auto'}
                ),
                width=12
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(figure={}, id="figPremier"),
                width=12
            )
        ])
    ])

    return pagina


@callback(
    Output(component_id="figPremier", component_property="figure"),
    Input(component_id="dpPremier", component_property="value")
)
def update_grafica(value_chosen):
    data_resumen = data.groupby("equipo", as_index=False).sum(numeric_only=True)
    columnas = ["pts", "gf", "gc", "df"]
    col_chosen = value_chosen
    if value_chosen == "all":
        col_chosen = columnas
    fig = px.line(data_resumen, x="equipo", y=col_chosen)
    return fig


if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dashboard(data)
    app.run_server(debug=True)
