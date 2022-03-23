#Aqui Resumire los codigos de los ejercicios correspondientes a listados,
#posiciones y operaciones con numeros de listas
Videojuegos = ['Smash','Super Mario','Halo','GOW','COD','Ark','GTAV']#Lista con la que trabajare practicamente todo
print(Videojuegos)
print("Mi videojuego favorito, sin duda es:" + Videojuegos[5])
print(Videojuegos[0] + " Corresponde a la posicion 0 de nuestro listado")#Muestreo del videojuego en la posicion 0
del Videojuegos[2]#Borramos un juego con el comando del
Videojuegos.remove('GOW')#Removemos juegos con el comando remove
print(Videojuegos)
VDJ1 = Videojuegos.pop(4)#Guardamos el juego de la posicion 4
VDJ2 = Videojuegos.pop(2)#Guardamos el juego de la posicion 2
Juegos_Fav = [VDJ1, VDJ2]#Almacenamos los juegos guardados en una nueva lista
print(Juegos_Fav)
Videojuegos.append('Rocket League')#Agregamos a la lista rocket league 
print(Videojuegos)
Videojuegos.insert(-3,'Minecraft')#Añadimos minecraft en la posicion -3 de la lista
print(Videojuegos)
Videojuegos.sort(reverse=False)#Acomoda los items de la lista alfabeticamente
print(Videojuegos)
Videojuegos.sort(reverse=True)#Acomoda los items de la lista de forma alfabeticamente empezando por z
print(Videojuegos)
Videojuegos_Tupla = tuple(Videojuegos)#nos convierte el listado en una tupla
print(type(Videojuegos_Tupla))#el comando type nos corroborará si el listado efectivamente es una tupla
#Operaciones con numeros de una lista
ListaConjunto = [13, 9, 21, 33, 49]
Operacion = ListaConjunto[1] + ListaConjunto[2] - ListaConjunto[0] * ListaConjunto[4]
print(Operacion)
