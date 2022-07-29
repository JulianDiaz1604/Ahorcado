from os import system
import juego
from listaPalabra.listarPalabras import *


menuprincipal = int(input("Menu Principal: \n0.Salir. \n1.Instrucciones. \n2.Eligir la complejidad. \n3.Agregar palabras a la lista. "
                          "\n4.Mostrar palabras.\n"))
system("cls")
puntos = 0

while menuprincipal != 0:

    if menuprincipal == 1:
        print("Bienvenido a las instrucciones.")
        print("1. Los simbolos ya mencionados restan 1 intento. ")
        print("2. Cada vez que se ingrese un caracter, se debe pintar la palabra y sus pistas ya descifradas")

    elif menuprincipal == 2:
        print("Ingresando a la complejidad.")
        opcion = int(input("\nComplejidad:\n1. Complejidad baja. \n2. Complejidad media. \n3. Complejidad alta. \n4.Volver al menu."
                           " \n\nIngrese una opcion: "))
        system("cls")
        while opcion != 0:
            if opcion == 1:
                palabra = filtro(1)
                print("\nJugando en complejidad baja\n")
                puntos = puntos + juego.juego(4, palabra)
            elif opcion == 2:
                palabra = filtro(2)
                print("\nJugando en complejidad media\n")
                puntos = puntos + juego.juego(6, palabra)
            elif opcion == 3:
                palabra = filtro(3)
                print("\nJugando en complejidad alta\n")
                puntos = puntos + juego.juego(8, palabra)

            elif opcion == 4:
                print("Volviendo al menu ....")

            else:
                print("Ingrese una complejidad valida")

            opcion = int(input("Complejidad: \n1. Complejidad baja \n2. Complejidad media \n3. Complejidad alta"))

    elif menuprincipal == 3:
        print("Agregando palabras a la lista")
        print("Ingrese la palabra que desea agregar a la lista: ")
        palabra = input()
        anadir(palabra)
        print("La palabra ingresada a la lista es: ", palabra)

    elif menuprincipal == 4:
        opcion = int(input("Complejidad:\n1. Complejidad baja. \n2. Complejidad media. \n3. Complejidad alta. \n4.Volver al menu."
                           " \n\nIngrese una opcion: "))
        mostrarLista(1)

    else:
        print("Por fevor digite una opcion correcta")
    menuprincipal = int(input(
        "Menu Principal: \n0.Salir. \n1.Instrucciones. \n2.Eligir la complejidad. \n3.Agregar palabras a la lista. \n"))