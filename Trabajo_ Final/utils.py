import numpy as np
import random
from xml.dom.pulldom import PROCESSING_INSTRUCTION

class Tablero:

    '''La clase Tablero se crea para generar los tableros de los jugadores'''                                                              
    
    #esloras=[4,3,3,2,2,2,1,1,1,1]
    esloras=[9,9,9,9,9,9,9,9,9]
    
    '''Dentro de la variable esloras hemos almacenado el numero de barcos con cada eslora:
    1 barco con 4 posiciones de eslora, 2 barcos de 3 posiciones, 3 barcos de dos posiciones y cuatro barcos de una posicion'''
    
    def __init__(self, nombre):
        
        '''Ambos tableros se crean vacios. 
        El tablero "propio" es el tablero del jugador y el tablero "disparo" es el de la máquina'''

        self.tablero_propio = np.full((10,10)," ")
        self.tablero_disparo = np.full((10,10)," ")
        self.nombre = nombre
        self.barcos = []
        for i in self.esloras:
            self.annadirbarco(i)
    
    def annadirbarco(self, eslora):
        '''En esta funcion se van a ir añadiendo los barcos de forma aleatoria
        como se describe en la clase Bote'''

        barco= Bote(eslora, self.tablero_propio)
        self.barcos.append(barco)
        
    def imprimir_tablero(self, tablero):

        '''Esta funcion imprime los tableros principales y añade en los margenes los titulos de filas
        y columnas para facilitar al usuario introducir las coordenadas en las que quiere disparar'''

        titulo = np.arange(0,10)
        tablero_titulos = np.insert(tablero, 0, titulo, axis= 0) 
        columna_titulo = np.append(["|"], titulo )
        tablero_titulos = np.insert(tablero_titulos, 0, columna_titulo, axis= 1) 
        print((f"Nombre del jugador :  {self.nombre}").title(), '\n')
        print(tablero_titulos)
        print("_______________________________________________", '\n')

    def imprimir_tableros_juego(self):

        '''Una vez creados los tableros, se añade el nombre del jugador
        y el tablero de disparos que corresponde al tablero de la máquina en el que iremos realizando disparos
        y se irán controlando aquellos barcos que han caido'''

        print("_______________________________________________", '\n')
        print("Tablero propio", '\n')
        self.imprimir_tablero(self.tablero_propio)
        print("Tablero de disparos", '\n')
        self.imprimir_tablero(self.tablero_disparo)
    
    def dado(self, coordenadas:tuple):

        '''Esta funcion recoge las coordenadas introducidas por el jugador donde desea disparar.
        se comprueba si en esas coordenadas existe alguna posicion de un barco.
        Si se encuentra "O" (barco) reescribe la posicion con una "X" y cambia el estado.
        Si no encuentra "O", sobreescribe con "@" para indicar que es agua'''

        if self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])] == "O":
            self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])] = "X"
            
            for i in self.barcos:
                if coordenadas in i.coordenadas:
                    if i.veces+1 == len(i.coordenadas):
                        i.estado = "hundido"
                        print('\n', "Hundido", '\n')
                        break
                    else:
                        i.veces += 1
                        i.estado = "tocado"
                        print('\n', "Tocado", '\n')
                        break
            if self.comprobar_fin():
                return 1000                                 #Este valor indicaría que ha terminado la partida
            else:
                return 1
        elif self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])] != " ":
            return 2        
        else:
            self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])] = "@"
            print('\n', "Agua", '\n')
            return 0

    def comprobar_fin(self):
        
        '''Con esta función se comprobará si queda aún algun barco por derribar '''

        if "O" in self.tablero_propio:
            return False
        else:
            return True
    
    def terminar_partida(self,jugador_oponente):

        '''Una vez que se han derribado todos los barcos, se indica quién ha ganado la partida y se muestran ambos tableros'''
        if self.nombre == 'Maquina':
            print('\n', "¡Has perdido!", '\n')
        else:
            print('\n', (f"¡ENHORABUENA, HAS GANADO LA PARTIDA {self.nombre}!").upper(), '\n')
        self.imprimir_tablero(self.tablero_propio)
        jugador_oponente.imprimir_tablero(jugador_oponente.tablero_propio)

class Bote:
    '''En esta clase se crean todos los barcos y la posicion en la que se colocaran aleatoriamente'''

    def __init__(self, eslora, tablero):
        self.estado=None
        self.coordenadas = self.buscar_posicion(eslora, tablero)
        self.veces= 0


    def buscar_posicion(self, eslora, tablero):

        '''Con esta funcion se colocan los barcos de forma aleatoria y se guarda la posicion de los mismos'''

        lista_coordenadas= []

        while True:
            orientacion = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            posicion = np.random.randint(10, size = 2)
            
            fila = posicion[0]
            columna = posicion[1]
            
            """Recogemos las 4 posiciones colindantes a posicion_actual ya que cuando se intenta acceder a una posicion de los bordes, como por ejemplo:
               colindantes_Norte = tablero[ fila : fila - eslora : -1, columna]
               colindantes_Norte = tablero[ 2 : (2 - 3) : -1, 4] -> tablero[2:-1:-1, 4], esto tendría que dar la posición (2,4) (1,4) (0,4) 
               y lo que devuelve en lugar del tablero con el disparo es un array vacio []
            """
            #norte
            if fila - eslora > 0:
                colindantes_Norte = tablero[ fila : fila - eslora : -1, columna]
            else:
                colindantes_Norte = tablero[ fila :: -1, columna]
            #Este
            colindantes_Este = tablero[fila, columna: columna + eslora]

            #Sur
            colindantes_Sur = tablero[fila:fila + eslora, columna]
            
            #Oeste
            if  columna - eslora > 0 :
                colindantes_Oeste = tablero[fila, columna: columna - eslora  :-1]
            else:
                colindantes_Oeste = tablero[fila, columna::-1]

            # Marcamos la posición en el barco y se recogen las coordenadas de dicho barco

            # Orientacion Norte
            if orientacion == 'N' and 0 <= fila - eslora + 1 < 10 and 'O' not in colindantes_Norte:
                if (fila-eslora) == -1:
                    tablero[fila::-1, columna] = 'O'         
                    for i in range(fila,-1,-1):
                        lista_coordenadas.append((i,columna))  
                else:
                    tablero[fila:(fila - eslora):-1, columna] = 'O'
                    for i in range(fila, fila-eslora,-1):
                        lista_coordenadas.append((i,columna))  
                break
            # Orientacion Este
            elif orientacion == 'E' and 0 <= columna + eslora <= 10 and 'O' not in colindantes_Este:
                tablero[fila, columna: columna + eslora] = 'O'
                for i in range(columna, columna + eslora):
                    lista_coordenadas.append((fila,i))
                break

            # Orientacion Sur
            elif orientacion == 'S' and 0 <= fila + eslora <= 10 and 'O' not in colindantes_Sur:
                tablero[fila:fila + eslora, columna] = 'O'
                for i in range(fila, fila + eslora):
                    lista_coordenadas.append((i,columna))
                break

            # Orientacion Oeste
            elif orientacion == 'O' and 0 <= (columna - eslora +1) < 10 and 'O' not in colindantes_Oeste:
                if (columna-eslora) == -1:
                    tablero[fila, columna::-1] = 'O'         
                    for i in range(columna,-1,-1):
                        lista_coordenadas.append((fila,i))  
                else:
                    tablero[fila, columna: (columna - eslora):-1] = 'O'
                    for i in range(columna,columna-eslora,-1):
                        lista_coordenadas.append((fila,i))  
                break

        return lista_coordenadas