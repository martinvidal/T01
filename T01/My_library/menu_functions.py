import os.path

def option1():
    archivo = input("""
    Ingrese el nombre del archivo de consultas 
    (debe estar presente en la misma carpeta de este programa)
    ingresa la letra "b" para volver al menú principal""")
    if archivo != "b":
        if not os.path.isfile(archivo):
            print("El archivo ingresado no existe")
            option1()
        else:
            with open(archivo, "r", encoding='utf-8') as file:
                reader = [l.rstrip() for l in file]
                print("archivo leido y guardado correctamente")
                return reader
