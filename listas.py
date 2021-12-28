def run():
    
    listadoNombres = []
    def ingresarNombre(): 
        nombre = input('Ingrese un nombre a la lista: ')
        listadoNombres.append(nombre)
        print(listadoNombres)
    
    def consultar():
        opcion = input("Ingrese 1 para agregar nombres: ")
        if opcion == "1":
            ingresarNombre()
            consultar()
        else:
            print('Se termino el programa')

    ingresarNombre()
    consultar()

     


if __name__ == '__main__':
    run()