import mysql.connector
import pandas as pd

data_df = pd.read_csv("dataset/premier-league.csv", index_col=0)
# Configura las credenciales de tu base de datos MySQL
config = {
    'user': 'root',
    'host': 'localhost',
    'database': 'PremierLeague',
    'raise_on_warnings': True
}

# Crea una conexión a la base de datos
conexion = mysql.connector.connect(**config)

# Crea un cursor para ejecutar consultas
cursor = conexion.cursor()

try:
# Define la estructura de la tabla
    estructura_tabla = (
        "CREATE TABLE IF NOT EXISTS posiciones ("
        "id INT AUTO_INCREMENT PRIMARY KEY,"
        "temporada VARCHAR(20),"
        "equipo VARCHAR(255),"
        "jj INT,"
        "jg INT,"
        "je INT,"
        "jp INT,"
        "gf INT,"
        "gc INT,"
        "df INT,"
        "pts INT"
        ")"
    )

    # Ejecuta la consulta para crear la tabla
    cursor.execute(estructura_tabla)
except:
    pass

# Itera sobre las filas del DataFrame e inserta los datos en MySQL
for index, fila in data_df.iterrows():
    consulta = "INSERT INTO posiciones (temporada, equipo, jj, jg, je, jp, gf, gc, df, pts) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (
        fila['Temporada'],
        fila['Equipo'],
        fila['JJ'],
        fila['JG'],
        fila['JE'],
        fila['JP'],
        fila['GF'],
        fila['GC'],
        fila['DF'],
        fila['PTS']
    )
    cursor.execute(consulta, valores)

# Confirma los cambios y cierra la conexión
conexion.commit()
conexion.close()