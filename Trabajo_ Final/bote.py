import random
from xml.dom.pulldom import PROCESSING_INSTRUCTION
import numpy as np

class Bote:

    def __init__(self,eslora,tablero):
        self.estado=None
        self.coordenadas = self.buscar_posicion(eslora,tablero)
        self.veces= 0


    def buscar_posicion(self,eslora,tablero):
        lista_coordenadas= []

        while True:
            orientacion = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            posicion = np.random.randint(10, size = 2)
            
            fila = posicion[0]
            columna = posicion[1]
            
            # Recogemos las 4 posiciones colindantes a posicion_actual
            """hacemos esto porque cuando python intenta acceder a unas posiciones de una matriz mediante código parecido al ejemplo:
            colindantes_Norte = tablero[ fila : fila - eslora : -1, columna]
            colindantes_Norte = tablero[ 2 : (2 - 3): -1, 4]
            (tablero[2:-1:-1,4], esto tendría que dar la posición (2,4) (1,4) (0,4) y no es capaz de dar datos, lo que genera es un array vacio []
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
                if ((fila-eslora)== -1):
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
                if ((columna-eslora)== -1):
                    tablero[fila, columna::-1] = 'O'         
                    for i in range(columna,-1,-1):
                        lista_coordenadas.append((fila,i))  
                else:
                    tablero[fila, columna: (columna - eslora):-1] = 'O'
                    for i in range(columna,columna-eslora,-1):
                        lista_coordenadas.append((fila,i))  
                break

        return lista_coordenadas
        
    