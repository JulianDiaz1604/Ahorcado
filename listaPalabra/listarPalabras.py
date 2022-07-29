import random
from modelo.Palabra import Palabra

barco = Palabra("barco", 1, False)
loca = Palabra("loca", 1, False)
electron = Palabra("electron", 2, False)
anatomia = Palabra("anatomia", 2, False)
esternocleidomastoideo = Palabra("esternocleidomastoideo", 3, False)
anticonstitucionalidad = Palabra("anticonstitucionalidad", 3, False)

complejidadBaja = [loca, barco]
complejidadMedia = [electron, anatomia]
complejidadAlta = [esternocleidomastoideo, anticonstitucionalidad]


def obtenerComplejidad(palabra):
    aux = len(palabra)
    if aux <= 5:
        return 1
    elif aux > 5 and aux <= 12:
        return 2
    else:
        return 3


def anadir(palabra):
    nuevaPalabra = Palabra(palabra, obtenerComplejidad(palabra), False)
    if (nuevaPalabra.complejidad == 1):
        complejidadBaja.append(nuevaPalabra)

    elif (nuevaPalabra.complejidad == 2):
        complejidadMedia.append(nuevaPalabra)

    else:
        complejidadAlta.append(nuevaPalabra)

    print("\nAñadida la palabra correctamente")


def filtro(complejidad):

    if (complejidad == 1):
        auxBajo = random.randint(0, len(complejidadBaja))
        if (sirve(complejidadBaja[auxBajo])):
            return complejidadBaja[auxBajo].getPalabra()
        else:
            filtro(complejidad)

    elif (complejidad == 2):
        auxMedio = random.randint(0, len(complejidadMedia))
        if (sirve(complejidadMedia[auxMedio])):
            return complejidadMedia[auxMedio].getPalabra()
        else:
            filtro(complejidad)

    elif (complejidad == 3):
        auxAlto = random.randint(0, len(complejidadAlta))
        if (sirve(complejidadAlta[auxAlto])):
            return complejidadAlta[auxAlto].getPalabra()

        else:
            filtro(complejidad)

    else:
        print("mmgvo, esto no es una complejidad")


def sirve(palabra):

    if not palabra.usada:
        return True
    else:
        return False


def mostrarLista(complejidad):
    if complejidad == 1:
        print(complejidadBaja)
    elif complejidad == 2:
        print(complejidadMedia)
    else:
        print(complejidadAlta)