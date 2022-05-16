from ast import Try
import numpy as np
import bote as b

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
        barco= b.Bote(eslora,self.tablero_propio)
        self.barcos.append(barco)
        

    def imprimir_tablero(self, tablero):
        titulo = np.arange(0,10)
        tablero_titulos = np.insert(tablero, 0, titulo, axis= 0) 
        columna_titulo = np.append(["|"], titulo )
        tablero_titulos = np.insert(tablero_titulos, 0, columna_titulo, axis= 1) 
        print(tablero_titulos)


    def imprimir_tableros_juego(self):
        print("___________________________________________________________")
        print(f"Nombre del jugador :  {self.nombre}")
        print("Tablero propio")
        self.imprimir_tablero(self.tablero_propio)
        print("Tablero de disparos")
        self.imprimir_tablero(self.tablero_disparo)
    


    def dado(self,coordenadas):
        try:                            #####MONICA
            if self.tablero_propio[coordenadas[0],coordenadas[1]]=="O":
                self.tablero_propio[coordenadas[0],coordenadas[1]]="X"
                
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
                self.tablero_propio[coordenadas[0],coordenadas[1]]="@"                                     ###Poner @ como agua en vez de -(?)
                print("Agua")
                return 0
        except Exception as ex:                           #### MONICA
            print(ex)


    def comprobar_posible_disparo(self,coordenadas):
        if self.tablero_disparo[coordenadas[0], coordenadas[1]] == " ":
            return True #puede disparar
        else:
            return False #ha sido disparado, hay que pedir otras coordenadas


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

