#pip instsall mysql-connector-python


#scikit-learn: proporciona herramientas para el aprendizaje automatico, incluye algoritmos para clasificacion, regresion, clustering y reduccion de dimensionalidad
#TensorFlow y PyTorch: bibliotecas para aprendizaje profundo permiten construir y entrenar redes neuronales
#Flask y Django: frameworks para desarrollo de aplicaciones web
#OS

import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',#reemplaza con una constraseña
            database='data'
        )
        
        print('Conexión exitosa')
        return conexion
    except mysql.connector.Error as error:
        print(f'Error de conexion a MySQL: {error}')
        return None
    except Exception as error:
        print(f'Error inesperado: {error}')
        return None
    #finally:
        #bloque finally, para futuras implementaciones, como cerrar la conexion.
        #if conexion.is_connected():
            #conexion.close()
            #print('Conexion cerrada')
            
            #pass
            
            
conexion = conectar_bd()
#conexion.close()