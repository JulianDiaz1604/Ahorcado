import time
from os import system


def juego(vidas, palabra):
    cont = 0
    letrasUsuario = ''
    vidasRestantes = vidas
    perdio = False

    while not perdio:
        system("cls")
        fallo = False
        fallas = 0
        print("\n")
        for letra in palabra:
            if letra in letrasUsuario:
                print(letra, end='')
            else:
                print("*", end='')
                fallas = fallas + 1

        if fallas == 0:
            print("\n\nFelicidades, Ganaste!!")
            break

        print("\n\nLetras Usadas: " + letrasUsuario)
        print("Vidas restantes: " + str(vidasRestantes))
        letraUsuario = input("\nIntroduce una letra: ").lower()
        time.sleep(0.5)

        if letraUsuario not in palabra:
            cont += 1
            print("Letra incorrecta\n")
            time.sleep(0.7)
            fallo = True
        elif letraUsuario in letrasUsuario:
            cont += 1
            print("La letra ya ha sido usada\n")
            time.sleep(0.7)
            fallo = True

        letrasUsuario = letrasUsuario + " " + letraUsuario

        if fallo:
            vidasRestantes = vidasRestantes - 1

        if cont == vidas:
            print("\nFin del juego")
            perdio = True

    puntos = calcularPuntos(cont, len(palabra))
    print("\nPuntuacion: " + str(puntos))
    input("\n\nPresione 'enter' para continuar")
    return puntos


def calcularPuntos(fallos, tamanoPalabra):
    puntos = 0
    if tamanoPalabra <= 5:
        puntos = puntos + 1
    elif tamanoPalabra > 5 and tamanoPalabra <= 12:
        puntos = puntos + 2
    else:
        puntos = puntos + 3

    if fallos == 0:
        if tamanoPalabra <= 12:
            puntos = puntos + 1
        else:
            puntos = puntos + 2

    return puntos
