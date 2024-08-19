import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('/home/dan/Desktop/Projects/ChileTrabajos/Assets/database.db')
cursor = conn.cursor()

def conectar_db(nombre_db):
    try:
        # Intenta conectarse a la base de datos
        conntest = sqlite3.connect(nombre_db)
        # Si la conexión es exitosa, retorna True
        return True
    except sqlite3.Error as e:
        # Si ocurre un error, imprime el mensaje de error
        print(f"Error al conectar a la base de datos: {e}")
        # Retorna False si la conexión falla
        return False


def getRecords():
    """
    Retorna todos los registros de la tabla Job.
    """
    try:
        cursor.execute('SELECT * FROM Job')
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"Error al seleccionar los registros: {e}")
        return None

# Función para añadir un registro a la tabla
def addRecord(day, link):
    try:
        cursor.execute('INSERT INTO Job (Day, Link) VALUES ("{}", "{}")'.format(day, link))
        conn.commit()
        # print("Registro añadido exitosamente")
    except sqlite3.Error as e:
        print(f"Error al añadir el registro: {e}")

# Función para borrar un registro de la tabla
def deleteRecord(day):
    try:
        # pico = 'DELETE FROM Job WHERE DATE(Day) <> DATE({})'.format(day)
        cursor.execute('DELETE FROM Job WHERE DATE(Day) != DATE("{}")'.format(day))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al borrar el registro: {e}")