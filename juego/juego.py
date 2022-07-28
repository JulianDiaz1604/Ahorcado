import time


def juego(vidas, palabra):

    cont = 0
    puntos = 0
    letrasUsuario = ''

    while cont != vidas:
        for letra in palabra:
            if letra in letrasUsuario:
                print(letra, end='')
            else:
                print("*", end='')
                cont += 1
        
        letraUsuario = input("Introduce una letra: ").lower()
        letrasUsuario = letrasUsuario + " " + letraUsuario

        if letraUsuario not in palabra:
            cont+=1
            print("Letra incorrecta")

        if cont == vidas:
            print("Fin del juego")

    if cont == 0:
        tamanoPalabra = len(palabra)
        if tamanoPalabra <= 12:
            puntos += 1
        else:
            puntos += 2
