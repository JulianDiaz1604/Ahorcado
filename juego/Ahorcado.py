import time
from os import system
import juego
from listaPalabra.listarPalabras import *

system("cls")
puntos = 0
menuprincipal = 1

while menuprincipal != 0:
    system("cls")

    menuprincipal = int(input("\n  AHORCADITO  \n"
                              "\nMenu Principal: \n\n1. Instrucciones. \n2. Jugar. \n3. Agregar palabras a la lista. "
                              "\n4. Ver puntuacion. \n0. Salir.\n\nIngrese una opcion: "))

    if menuprincipal == 1:
        system("cls")
        print("\nBienvenido a las instrucciones.\n")
        print("1. Las letras repetidas o que no esten en la palabra restan 1 intento. ")
        print("2. Si adivina una palabra sin equivocarse tiene un bonus de acuerdo a la complejidad:\n"
              "   Complejidad baja y media suman un punto\n"
              "   Complejidad alta suma dos puntos.")
        print("3. Los puntos de acuerdo a la complejidad de la plabra son:\n"
              "   Complejidad baja = 1 punto\n"
              "   Complejidad media = 2 punto\n"
              "   Complejidad alta = 3 punto\n")
        time.sleep(2)
        input("\nPresione la tecla 'enter' para continuar.")
        continue

    elif menuprincipal == 2:
        system("cls")
        print("\nIngresando a la complejidad.")
        opcion = int(input("\nComplejidad:\n1. Complejidad baja. \n2. Complejidad media. \n3. Complejidad alta. \n4. Volver al menu."
                           " \n\nIngrese una opcion: "))
        system("cls")
        while opcion != 4:
            if opcion == 1:
                palabra = filtro(1)
                print("\nJugando en complejidad baja\n")
                puntos = puntos + juego.juego(4, palabra)
                break
            elif opcion == 2:
                palabra = filtro(2)
                print("\nJugando en complejidad media\n")
                puntos = puntos + juego.juego(6, palabra)
                break
            elif opcion == 3:
                palabra = filtro(3)
                print("\nJugando en complejidad alta\n")
                puntos = puntos + juego.juego(8, palabra)
                break
            elif opcion == 4:
                print("Volviendo al menu ....")
                break

            else:
                print("Ingrese una complejidad valida")


    elif menuprincipal == 3:
        system("cls")
        print("\nAgregando palabras a la lista\n")
        print("Ingrese la palabra que desea agregar a la lista: ")
        palabra = input()
        anadir(palabra)
        print("\nLa palabra ingresada a la lista es: ", palabra)
        input("\n\nPresione 'enter' para continuar")

    elif menuprincipal == 4:
        system("cls")
        print("\n\nPuntuacion: " + str(puntos))
        input("\n\nPresione 'enter' para continuar.")

    elif menuprincipal == 0:
        print("\n\nSaliendo...")
        time.sleep(2)

    else:
        print("Por fevor digite una opcion correcta")