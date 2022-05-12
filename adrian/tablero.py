import numpy as np
import random

class Tablero:
    
    cuerpo=np.full((10,10),"")                                               ###Este sera el tablero donde iran nuestros barcos
    copia=np.full((10,10),"")                                                ###Este sera el tablero donde iran nuestros los disparos del enemigo
                                                                            ### Idea magica, para comprobar si se ha disparado, cuando se dispare hacer esto
                                                                            ###         if coordenadas in tablero.copia == "": dispara ; si no vuelve a elegir coordenadas
    esloras=[4,3,3,2,2,2,1,1,1,1]                                           ### Es el numero de barcos con cada eslora : 1 de 4, 2 de 3, 3 de 2 , 4 de 1
    barcos=[]
    
    def __init__(self,nombre):
        self.nombre=nombre
        for i in self.esloras:
            self.annadirbarco(i)
    
    def annadirbarco(self,eslora):
        bote=Bote(eslora,self.cuerpo)
        self.barcos.append(bote)
        

    def dado(self,coordenadas:tuple):
        if self.cuerpo[coordenadas[0]][coordenadas[1]]=="O":
            self.cuerpo[coordenadas[0]][coordenadas[1]]="X"
            self.copia[coordenadas[0]][coordenadas[1]]="X"


            for i in self.barcos:
                if coordenadas in i.coordenadas:
                    if i.veces+1==len(self.coordenadas):
                        i.estado="hundido"                                  ###Pondre esto para a la hora de imprimir el mensaje por pantalla hacer print("Barco",estado)
                        """
                        Poner sonidito barco hundido
                        """
                    else:
                        i.veces+=1
                        i.estado="tocado"
                        print("Tocado")                                     ###Pondre esto para a la hora de imprimir el mensaje por pantalla hacer print("Barco",estado)
                        """ 
                        Poner sonidito barco tocado
                        """

            if self.comprobar_fin():
                self.terminar_partida()
            else:
                pass
        else:
            self.copia[coordenadas]="@"                                     ###Poner @ como agua en vez de -(?)
            print("Agua")

    def comprobar_fin(self):
        if "X" in self.cuerpo:
            return False
        else:
            return True
    
    def terminar_partida():
        pass                                                                ### annadir pantalla final y menu sobre que hacer ahora
        
class Bote:
    coordenadas=[]                                                          ### contiene tuplas con coordenadas del barco
    estado=None
    veces=[0]                                                               ### veces tocado 
    
    def __init__(self,eslora,tablero):
        while True:
            x=self.buscar_posicion(eslora,tablero)                                  ###Si funciona devuelve lista con tuplas(coordenadas), si no, devuelve None
            if type(x)==list:
                self.coordenadas.append(x)
                break
            else:
                continue

    def buscar_posicion(self,eslora,tablero):
        x=[]
        while len(x)<eslora:
            orientacion = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            posicion_actual = np.random.randint(10, size = 2)
            
            fila = posicion_actual[0]
            col = posicion_actual[1]
            
            # Recogemos las 4 posiciones colindantes a posicion_actual
            colindantes_Norte = tablero[fila:fila - eslora:-1, col]
            colindantes_Este = tablero[fila, col: col + eslora]
            colindantes_Sur = tablero[fila:fila + eslora, col]
            colindantes_Oeste = tablero[fila, col: col - eslora:-1]
            ##########Falta comprobar en los tres primeros la comprobacion del ultimo

            # Comprobar si esas posiciones son validas
            # Orientacion Norte
            if orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in colindantes_Norte:
                tablero[fila:fila - eslora:-1, col] = 'O'
                for i in range(fila,fila-eslora+1,-1):
                    x.append((i,col))

            # Orientacion Este
            elif orientacion == 'E' and 0 <= col + eslora < 10 and 'O' not in colindantes_Este:
                tablero[fila, col: col + eslora] = 'O'
                for i in range(col,col+eslora+1):
                    x.append((fila,i))
                

            # Orientacion Sur
            elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in colindantes_Sur:
                tablero[fila:fila + eslora, col] = 'O'
                for i in range(fila,fila+eslora+1):
                    x.append((i,col))
                

            # Orientacion Oeste
            elif orientacion == 'O' and 0 <= (col - eslora+1) < 10 and 'O' not in colindantes_Oeste:
                if ((col-eslora)== -1):
                    tablero[fila, col::-1] = 'O'         
                    for i in range(col,-1,-1):
                        x.append((fila,i))  
                else:
                    tablero[fila, col: (col - eslora):-1] = 'O'
                    for i in range(col,col-eslora,-1):
                        x.append((fila,i))  
                

            else:
                continue
        return x
        
    