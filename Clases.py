class EstadisticasEquipo:
    def __init__(self, data):
        self.data = data

    def datos_equipo(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo

    def max_puntos(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['PTS'].idxmax()]

    def min_puntos(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['PTS'].idxmin()]

    def max_goles(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['GF'].idxmax()]

    def min_goles_temporada(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['GF'].idxmin()]

    def max_goles_contra(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['GC'].idxmax()]

    def min_goles_contra(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['GC'].idxmin()]

    def campeon(self, temporada):
        datos_temporada = self.data[self.data['Temporada'] == temporada]
        ganador = datos_temporada.loc[datos_temporada['PTS'].idxmax()]
        return ganador['Equipo']

    def max_dif_goles(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['DF'].idxmax()]

    def min_dif_goles(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        return datos_equipo.loc[datos_equipo['DF'].idxmin()]

    def promedio_goles(self, nombre_equipo):
        datos_equipo = self.data[self.data['Equipo'] == nombre_equipo]
        promedio_goles_anotados = datos_equipo['GF'].mean()
        return promedio_goles_anotados

    def promedio_goles_en_contra(self, nombre_equipo):
        datos_temporada = self.data[self.data['Equipo'] == nombre_equipo]
        promedio_goles_en_contra = datos_temporada['GC'].mean()
        return promedio_goles_en_contra
