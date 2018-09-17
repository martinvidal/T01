
from My_library import queries, menu_functions
import os.path

data_size = "small"
path = "data/{}/".format(data_size)
file = queries.load_database(path, "Flights")
file2 = queries.load_database(path, "Airports")
file3 = queries.load_database(path, "Travels")
file4 = queries.load_database(path, "Passengers")
print(queries.passenger_miles(file4, file2, file, file3))


if __name__ == '__main__':
    try:
        while True:
            option = input("""
            Cruncher Flights
                Menú:
                    Opciones:
                    (1)Abrir un archivo de consultas
                    (2)Ingresar consulta
                    (3)Leer archivo de resultados""")
            if option not in "123":
                print("Ingrese una opción valida")
            else:
                if option == "1":
                    queries = menu_functions.option1()
                    for query in queries:
                        print("({}) {}".format(queries.index(query)+1, query))
                    opciones = input("ingresa él o los indices de las consultas"
                                     "que desea realizar (en la forma \"1,2,10,"
                                     "14\" o \"0\" para realizarlas todas")


                elif option == "2":
                    pass
                elif option == "3":
                    pass
            # rellenar esta parte con el llamado a sus funciones
            # sigue corriendo el uso restringido en toda situacion
            # de los for/while/etc dentro de este main a excepcion
            # del que se encuentra arriba, por lo que no se puede
            # agregar ninguno mas

    # no es necesario que hagan una parte para salir del menu
    except KeyboardInterrupt():
        exit()
