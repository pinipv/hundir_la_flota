import numpy as np
import random

class Tablero:
    
                                                  
                                                                            ### Idea magica, para comprobar si se ha disparado, cuando se dispare hacer esto
                                                                            ###         if coordenadas in tablero.copia == "": dispara ; si no vuelve a elegir coordenadas
    esloras=[4,3,3,2,2,2,1,1,1,1]                                           ### Es el numero de barcos con cada eslora : 1 de 4, 2 de 3, 3 de 2 , 4 de 1
    
    
    def __init__(self,nombre):
        self.cuerpo=np.full((10,10)," ")                                                ###Este sera el tablero donde iran nuestros barcos
        self.copia=np.full((10,10)," ")                                                 ###Este sera el tablero donde iran nuestros disparos al enemigo
        self.nombre=nombre
        self.barcos=[]
        for i in self.esloras:
            self.annadirbarco(i)
    
    def annadirbarco(self,eslora):
        bote=Bote(eslora,self.cuerpo)
        self.barcos.append(bote)
        

    def dado(self,coordenadas:tuple):
        if self.cuerpo[int(coordenadas[0]),int(coordenadas[1])]=="O":
            self.cuerpo[int(coordenadas[0]),int(coordenadas[1])]="X"
            


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
                return 1
        else:
            self.cuerpo[int(coordenadas[0]),int(coordenadas[1])]="@"                                     ###Poner @ como agua en vez de -(?)
            print("Agua")
            return 0

    def comprobar_fin(self):
        if "X" in self.cuerpo:
            return False
        else:
            return True
    
    def terminar_partida():
        pass                                                                ### annadir pantalla final y menu sobre que hacer ahora
        
