import random
class Palabra:

    def __init__(self, palabra,complejidad,usada):
        self.palabra = palabra
        self.complejidad=complejidad
        self.usada =False


complejidadBaja = [loca, barco]
complejidadMedia = [electron, anatomia]
complejidadAlta = [esternocleidomastoideo,anticonstitucionalidad]
baja=len(complejidadBaja)
media = len(complejidadMedia)
alta=len(complejidadAlta)






electron = Palabra("electron",2,false)
esternocleidomastoideo = Palabra("esternocleidomastoideo",3,false)
anatomia = Palabra("anatomia",2,false)
anticonstitucionalidad =Palabra("anticonstitucionalidad",3,false)
barco = Palabra("barco",1,false)
loca = Palabra("loca",1,false)
palabra=Palabra

def Complejidad(palabra):
   aux = len(palabra)
   if aux <= 5:
       return 1
   elif aux > 5:
       if aux <12:
           return 2
   else:
       return 3

def Añadir(palabras):
    NuevaPalabra = Palabra(palabras,Complejidad(palabras),false)
    if(NuevaPalabra.complejidad==1):
        complejidadBaja.append(NuevaPalabra)

    elif(NuevaPalabra.complejidad==2):
        complejidadMedia.append(NuevaPalabra)

    else:
        complejidadAlta.append(NuevaPalabra)
    print("añadida la palabra correctamente")

def filtro(comple):
    if(comple == 1):
        auxBajo = random.randint(0, baja)
        if(sirve(complejidadBaja[auxBajo])):
            complejidadBaja[auxBajo]
        else:
            filtro(comple)

    elif(comple == 2):
        auxmedio = random.randint(0, media)
        if(sirve(complejidadMedia[auxmedio])):
            complejidadMedia[auxmedio]
        else:
            filtro(comple)
    elif(comple == 3):
        auxalto = random.randint(0, alta)
        if(sirve(complejidadAlta[auxalto])):
           complejidadAlta[auxalto]

        else:
            filtro(comple)
    else:
        print("mmgvo, esto no es una complejidad")

def sirve(palabra):
    palabra = Palabra()
    if(palabra.usada == false):
        return true
    else:
        return false
