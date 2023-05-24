#Ejercicio 19 de pilas
from pila import Pila
class Peliculas():

    def __init__(self, titulo, anio, estudio):
        self.__titulo = titulo
        self.__anio = anio
        self.__estudio = estudio
    
    def get_titulo(self):
        return self.__titulo

    def get_anio(self):
        return self.__anio
    def get_estudio(self):
        return self.__estudio
       

peliculass= [
    Peliculas('Black Panther', 2018, 'Marvel Studios'),
    Peliculas('Avengers:Age of Ultron', 2015, 'Marvel Studios'),
    Peliculas('Frozen II',2019,'Pixar Studios'),
    Peliculas('Fast And Furious 7',2015, 'Universal Pictures'),
    Peliculas('The Avengers', 2013, 'Marvel Studios'),
    Peliculas('El Rey Leon', 2019, 'Walt Disney Pictures'),
    Peliculas('Jurassic World',2015,'Universal Pictures'),
    Peliculas('Avengers: Infinity War',2018,'Marvel Studios'),
    Peliculas('Star Wars: The Force Awakens', 2015, 'Lucasfilm' ),
    Peliculas('Avengers:Endgame', 2019, 'Marvel Studios'),
    ]


pila_1 = Pila()
for Peliculas in peliculass:
    pila_1.push(Peliculas)
estrenos18=0
while pila_1.size() > 0:
    dato = pila_1.pop()
    if dato.get_anio() == 2014:
        print(dato.get_titulo(), 'se estreno en 2014')
    if dato.get_anio() == 2018:
        estrenos18 = estrenos18 + 1
    if (dato.get_anio() == 2016) and (dato.get_estudio()=='Marvel Studios'):
        print(dato.get_titulo())

print('Las cantidad de peliculas estrenadas en 2018 es: ', estrenos18 )



#Ejercicio 
class Personajes():
    def __init__(self, nombre,cantidad_de_apariciones):
         self.__nombre = nombre
         self.__cantidad_de_apariciones = cantidad_de_apariciones
    def get_nombre(self):
        return self.__nombre
    def get_cantidad_de_apariciones(self):
        return self.__cantidad_de_apariciones
personajes= [
    Personajes('Rocket Racoon', 6),
    Personajes('Groot', 6),
    Personajes('Black Widow', 10),
    Personajes('Steve Rogers',11),
    Personajes('Tony Stark', 10),
    Personajes('Thor',8),
    Personajes('Hulk',9),
    ]

pila_2=Pila()
for Personajes in personajes:
    pila_2.push(Personajes)
posicion=0    
while pila_2.size() > 0:
    Superheroe= pila_2.pop()
    posicion= posicion+1
    if (Superheroe.get_nombre()=='Rocket Racoon') or (Superheroe.get_nombre()=='Groot'):
        print(Superheroe.get_nombre(),' se encuentra en la posicion ',posicion)
    if Superheroe.get_cantidad_de_apariciones() >= 5:
        print(Superheroe.get_nombre(), 'Ha aparecido mas de 5 veces en el MCU, Ha aparecido ',Superheroe.get_cantidad_de_apariciones(),' veces.')
    if Superheroe.get_nombre() == 'Black Widow':
          print('La viuda negra ha aparecido en ',Superheroe.get_cantidad_de_apariciones(),' peliculas.')
    if (Superheroe.get_nombre()[0]== 'C') or (Superheroe.get_nombre()[0]=='D') or (Superheroe.get_nombre()[0]=='G'):
        print(Superheroe.get_nombre())