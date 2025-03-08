from conexionData import conectar_db
import MySQLdb

conexion = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='data')

#reemplaza con una constraseña
#print(conexion)

def crear_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    sql = 'INSERT INTO pacientes (nombre, apellido) VALUES(%s, %s)'
    valores = (nombre, apellido)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f'Tus datos se han guardado con exito')
    cursor.close()
    
def leer_registros(conexion):
    cursor = conexion.cursor()
    sql = 'SELECT * FROM pacientes'
    cursor.execute(sql)
    pacientes = cursor.fetchall() #obtiene los datos y los imprime
    for paciente in pacientes:
        print(paciente)
    cursor.close()
   
def leer_registro_enfermeros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM enfermeros")
    enfermeros = cursor.fetchall()
    for enfermero in enfermeros:
        print(enfermero)
    cursor.close()   
    
def actualizar_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    try:
        sql = 'UPDATE pacientes SET nombre = %s, apellido = %s WHERE id = %s'
        valores = (nombre, apellido)
        cursor.execute(sql, valores)
        conexion.commit()
        print('Se ha actualizado los datos correctamente')
    except MySQLdb.connector.Error as error:
        print(f'Error al actualizar el registro {error}')
    finally:
        cursor.close()
        



def crear_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    sql = 'INSERT INTO enfermeros (nombre, apellido) VALUES(%s, %s)'
    valores = (nombre, apellido)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f'Tus datos se han guardado con exito')
    cursor.close()
    
def leer_registros(conexion):
    cursor = conexion.cursor()
    sql = 'SELECT * FROM enfermeros'
    cursor.execute(sql)
    enfermeros = cursor.fetchall() #obtiene los datos y los imprime
    for enfermero in enfermeros:
        print(enfermero)
    cursor.close()
   
def leer_registro_enfermeros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM enfermeros")
    enfermeros = cursor.fetchall()
    for enfermero in enfermeros:
        print(enfermero)
    cursor.close()   
    
def actualizar_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    try:
        sql = 'UPDATE enfermeros SET nombre = %s, apellido = %s WHERE id = %s'
        valores = (nombre, apellido)
        cursor.execute(sql, valores)
        conexion.commit()
        print('Se ha actualizado los datos correctamente')
    except MySQLdb.connector.Error as error:
        print(f'Error al actualizar el registro {error}')
    finally:
        cursor.close()        
    
#import MySQLdb

#db = MySQLdb.connect(password="", user="root", db="data")
#c = db.cursor()
#c.execute("SELECT * FROM pacientes")
#c.close()
#db.close()
    
#print(db)
    
    
    
     
crear_registro(conexion, 'Juan', 'Perez')
#leer_registros(conexion)

conexion.close()