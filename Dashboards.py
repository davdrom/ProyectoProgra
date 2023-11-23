import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table, callback, Input, Output

data = pd.read_csv("dataset/premier-league.csv", index_col=0)


def dashboard(data):
    data_resumen = data.groupby("Equipo", as_index=False).sum(numeric_only=True)
    pagina = html.Div([
        html.H2("Dashboard Premier League"),
        html.P("Objetivo: Mostrar los resultados de la Premier League"),
        html.Hr(),
        dcc.Dropdown(options=["PTS", "GF", "GC", "DF", "all"], value="all", id="dpPremier"),
        dash_table.DataTable(data=data_resumen.to_dict("records"),
                            page_size=15, id="tblPremier"),
        dcc.Graph(figure={}, id="figPremier")
    ])
    return pagina


@callback(
    Output(component_id="figPremier", component_property="figure"),
    Input(component_id="dpPremier", component_property="value")
)
def update_grafica(value_chosen):
    data_resumen = data.groupby("Equipo", as_index=False).sum(numeric_only=True)
    columnas = ["PTS", "GF", "GC", "DF"]
    col_chosen = value_chosen
    if value_chosen == "all":
        col_chosen = columnas
    fig = px.line(data_resumen, x="Equipo", y=col_chosen)
    return fig


if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = dashboard(data)
    app.run(debug=True)
