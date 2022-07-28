menuprincipal = int(input("Menu Principal: \n0.Salir. \n1.Instrucciones. \n2.Eligir la complejidad. \n3.Agregar palabras a la lista. \n"))

while menuprincipal != 0:

    if menuprincipal == 1:
        print("Bienvenido a las instrucciones.")
        print("1. Los simbolos ya mencionados restan 1 intento. ")
        print("2. Cada vez que se ingrese un caracter, se debe pintar la palabra y sus pistas ya descifradas")

    elif menuprincipal == 2:
        print("Ingresando a la complejidad.")
        complejidad = int(input("Complejidad:\n1. Complejidad baja. \n2. Complejidad media. \n3. Complejidad alta. \n4.Volve al menu. \n"))
        while complejidad != 0:
            if complejidad == 1:
                print("Jugando en complejidad baja")
            elif complejidad == 2:
                print("Jugando en complejidad media")
            elif complejidad == 3 :
                print("Jugando en complejidad alta")

            elif complejidad == 4:
                print("Volviendo al menu ....")

            else:
                print("Ingrese una complejidad valida")


            complejidad = int(input("Complejidad: \n1. Complejidad baja \n2. Complejidad media \n3. Complejidad alta"))

    elif menuprincipal == 3:
        print("Agregando palabras a la lista")
        print("Ingrese la palabra que desea agregar a la lista: ")
        palabra = input()
        print("La palabra ingresada a la lista es: ", palabra)

    else:
        print("Por fevor digite una opcion correcta")
    menuprincipal = int(input(
        "Menu Principal: \n0.Salir. \n1.Instrucciones. \n2.Eligir la complejidad. \n3.Agregar palabras a la lista. \n"))