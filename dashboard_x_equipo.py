import pandas as pd
import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, data):
        self.data = data

    def puntos_por_temporada(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]

        plt.figure(figsize=(10, 6))
        plt.plot(datos_equipo['Temporada'], datos_equipo['PTS'], marker='o', linestyle='-', color='green')
        plt.xlabel('Temporada')
        plt.ylabel('Puntos')
        plt.title(f'Puntos por temporada - {nombre_equipo}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def diferencia_goles_temporada(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]

        plt.figure(figsize=(10, 6))
        plt.plot(datos_equipo['Temporada'], datos_equipo['DF'], marker='o', linestyle='-', color='blue')
        plt.xlabel('Temporada')
        plt.ylabel('Diferencia de Goles')
        plt.title(f'Diferencia de Goles por temporada - {nombre_equipo}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


# pruebas
data = pd.read_csv("dataset/premier-league.csv", index_col=0)
g = Graficos(data)

nombre_equipo = "Newcastle United"
g.puntos_por_temporada(nombre_equipo)
g.diferencia_goles_temporada(nombre_equipo)
