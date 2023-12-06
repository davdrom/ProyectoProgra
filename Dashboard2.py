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
    # Obtener lista de equipos y temporadas
    equipos = data["equipo"].unique()
    temporadas = data["temporada"].unique()

    # Diseño utilizando componentes de Dash Bootstrap
    pagina = dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Dashboard Premier League"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.P(
                "Objetivo: Mostrar las estadísticas históricas de los equipos que han jugado en la Premier League"),
                    width=12)
        ]),
        dbc.Row([
            dbc.Col(html.Hr(), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    options=[{"label": equipo, "value": equipo} for equipo in equipos],
                    value=equipos[0],  # Establecer el valor predeterminado al primer equipo
                    id="dpEquipo",
                    multi=False,
                    style={"margin-bottom": "10px"}
                ),
                width=6
            ),
            dbc.Col(
                dcc.Dropdown(
                    options=[{"label": temporada, "value": temporada} for temporada in temporadas],
                    value=temporadas[0],  # Establecer el valor predeterminado a la primera temporada
                    id="dpTemporada",
                    multi=False,
                    style={"margin-bottom": "10px"}
                ),
                width=6
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                    id="tblEstadisticas",
                    columns=[{"name": col, "id": col} for col in data.columns if col != "id"],
                    # Excluir la columna "id"
                    style_table={'overflowX': 'auto'}
                ),
                width=12
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id="graficoEstadisticas"),
                width=12
            )
        ])
    ])

    return pagina


@callback(
    [Output(component_id="tblEstadisticas", component_property="data"),
     Output(component_id="graficoEstadisticas", component_property="figure")],
    [Input(component_id="dpEquipo", component_property="value"),
     Input(component_id="dpTemporada", component_property="value")]
)
def update_estadisticas(selected_equipo, selected_temporada):
    # Convertir la columna "temporada" a tipo string para la comparación
    data["temporada"] = data["temporada"].astype(str)

    # Filtrar los datos utilizando el método query
    equipo_temporada_data = data.query(f"equipo == '{selected_equipo}' and temporada == '{selected_temporada}'")

    # Configurar los datos de la tabla
    data_table = equipo_temporada_data.to_dict("records")

    # Configurar el gráfico de líneas
    fig = px.scatter(equipo_temporada_data, x="temporada", y=["pts", "gf", "gc", "df"],
                  title=f"Estadísticas de {selected_equipo} - Temporada {selected_temporada}")

    return data_table, fig


if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dashboard(data)
    app.run_server(debug=True)
