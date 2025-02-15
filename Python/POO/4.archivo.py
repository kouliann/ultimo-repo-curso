def app():
    archivo = open('achivo.txt', 'w')
    for i in range(0,10):
        archivo.write(f'esta es la linea {i}\n')
    archivo.close() #cerra archivo
    
    
    #'w': write, solo escritura (sobreescribe el archivo si existe)
    #'r': read, solo lectura (por defecto)
    #'a': Añadir (añade al final de los archivos)
    #'x': crear (crea un nuevo archivo, si ya existe, lanza un error)
    #'b': binario (para abrir archivos binarios)
    #'+': leer y escribir
    
app()