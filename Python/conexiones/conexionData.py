#pip instsall mysql-connector-python


#scikit-learn: proporciona herramientas para el aprendizaje automatico, incluye algoritmos para clasificacion, regresion, clustering y reduccion de dimensionalidad
#TensorFlow y PyTorch: bibliotecas para aprendizaje profundo permiten construir y entrenar redes neuronales
#Flask y Django: frameworks para desarrollo de aplicaciones web
#OS

import MySQLdb

def conectar_db():
    try:
        conexion = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="",
            db="data"
        )
        print("Conexión exitosa")
        return conexion
    except MySQLdb.Error as e:
        print(f"Error de conexión: {e}")
        return None

conexion = conectar_db()

if conexion:
    try:
        cursor = conexion.cursor()  # Corrected: Use conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila)

    except MySQLdb.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        cursor.close()
        conexion.close()
        print("Conexión cerrada")


# no hay que olvidarse de liberar el cursor y la conexión para evitar fugas de memoria
cursor.close()