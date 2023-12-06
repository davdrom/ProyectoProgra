import mysql.connector
import pandas as pd

class EstadisticasEquipo:

    def __init__(self, base_datos_config):
        self.base_datos_config = base_datos_config
        self.estadisticas_df = None
        self.cargar_estadisticas()

    def cargar_estadisticas(self):
        # Cargar estadísticas de todos los equipos desde la base de datos
        conexion = mysql.connector.connect(**self.base_datos_config)

        # Obtener datos de la tabla posiciones para todos los equipos
        consulta = "SELECT * FROM posiciones"
        self.estadisticas_df = pd.read_sql_query(consulta, conexion)

        # Obtener datos de la tabla equipos para el nombre de los equipos
        consulta_equipos = "SELECT DISTINCT equipo FROM posiciones"
        equipos_df = pd.read_sql_query(consulta_equipos, conexion)

        # Merge de los datos para asegurar que todos los equipos estén presentes
        self.estadisticas_df = equipos_df.merge(self.estadisticas_df, on='equipo', how='left')

        conexion.close()

    def obtener_estadisticas(self):
        return self.estadisticas_df

    def obtener_promedio_puntos(self):
        return self.estadisticas_df['pts'].mean()

    def obtener_total_goles_a_favor(self):
        return self.estadisticas_df['gf'].sum()

    def obtener_estadisticas_resumidas(self):
        return self.estadisticas_df.groupby("equipo", as_index=False).sum(numeric_only=True)
