import numpy as np
import random


class Bote:

    def __init__(self, eslora, tablero):
        self.estado = None
        self.coordenadas = self.buscar_posicion(eslora,tablero)
        self.veces= 0 # contador no es necesario array


    def buscar_posicion(self,eslora, tablero):
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


class Tablero:
                                                                  
    esloras=[4,3,3,2,2,2,1,1,1,1]         ### Es el numero de barcos con cada eslora : 1 de 4, 2 de 3, 3 de 2 , 4 de 1

    
    def __init__(self,nombre):
        self.tablero_propio= np.full((10,10)," ")               ###Este sera el tablero donde iran nuestros barcos
        self.tablero_disparo= np.full((10,10)," ")              ###Este sera el tablero donde iran nuestros disparos al enemigo
        self.nombre= nombre
        self.barcos= []
        for i in self.esloras:
            self.annadirbarco(i)
    


    def annadirbarco(self,eslora):
        barco= Bote(eslora,self.tablero_propio) #mgr
        self.barcos.append(barco)
        

    def imprimir_tablero(self, tablero):                        ### ccbb Titulos
        titulo = np.arange(0,10)
        tablero_titulos = np.insert(tablero, 0, titulo, axis= 0) 
        columna_titulo = np.append(["|"], titulo )
        tablero_titulos = np.insert(tablero_titulos, 0, columna_titulo, axis= 1) 
        print(tablero_titulos)

    def imprimir_tableros_juego(self):          #cbb
        print("___________________________________________________________")
        print(f"Nombre del jugador :  {self.nombre}")
        print("Tablero propio")
        self.imprimir_tablero(self.tablero_propio)
        print("Tablero de disparos")
        self.imprimir_tablero(self.tablero_disparo)
    


    def dado(self,coordenadas:tuple):
        if self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])]=="O":
            self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])]="X"
            
            for i in self.barcos:
                if coordenadas in i.coordenadas:
                    if i.veces+1 == len(i.coordenadas):
                        i.estado="hundido"
                        print("Hundido")                                  ###Pondre esto para a la hora de imprimir el mensaje por pantalla hacer print("Barco",estado)
                        break            #para que no este iterando en todos los barcos una vez localizado el hundido
                    else:
                        i.veces+=1
                        i.estado="tocado"
                        print("Tocado")                                     ###Pondre esto para a la hora de imprimir el mensaje por pantalla hacer print("Barco",estado)
                        break
            if self.comprobar_fin():
                return 1000                                 #Este valor indicaría que ha terminado la partida _cbba
            else:
                return 1
        else:
            self.tablero_propio[int(coordenadas[0]),int(coordenadas[1])]="@"                                     ###Poner @ como agua en vez de -(?)
            print("Agua")
            return 0


    def comprobar_fin(self):                                            ##Comprobar si queda alguna coordenada sin golpear
        if "O" in self.tablero_propio:
            return False
        else:
            return True
    
    def terminar_partida(self,jugador_oponente):
        print(f"Enhorabuena has ganado la partida {self.nombre} ")
        self.imprimir_tableros_juego()
        print("Se imprimen también los tableros del oponente")
        jugador_oponente.imprimir_tableros_juego()

