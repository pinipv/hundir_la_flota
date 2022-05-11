import numpy as np

class Tablero:
    
    cuerpo=np.full((10,10),0)                                               ###Este sera el tablero donde iran nuestros barcos
    copia=np.full((10,10),0)                                                ###Este sera el tablero donde iran nuestros los disparos del enemigo
                                                                            ### Idea magica, para comprobar si se ha disparado, cuando se dispare hacer esto
                                                                            ###         if coordenadas in tablero.copia == "": dispara ; si no vuelve a elegir coordenadas
    esloras=[4,3,3,2,2,2,1,1,1,1]                                           ### Es el numero de barcos con cada eslora : 1 de 4, 2 de 3, 3 de 2 , 4 de 1
    barcos=[]
    
    def __init__(self,nombre):
        self.nombre=nombre
        for i in self.esloras:
            self.annadirbarco(i)
    
    def annadirbarco(self,eslora):
        self.barcos.appned(Bote(eslora))

    def dado(self,coordenadas:tuple):
        if self.cuerpo[[tuple]]=="O":
            self.cuerpo[tuple]="X"
            self.copia[tuple]="X"


            for i in self.barcos:
                if coordenadas in i.coordeandas:
                    if i.veces+1==len(self.coordenadas):
                        i.estado="hundido"                                  ###Pondre esto para a la hora de imprimir el mensaje por pantalla hacer print("Barco",estado)
                        """
                        Poner sonidito barco hundido
                        """
                    else:
                        self.veces+=1
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
    
    def __init__(self,eslora):
        while True:
            x=self.buscar_posicion(eslora)                                  ###Si funciona devuelve lista con tuplas(coordenadas), si no, devuelve None
            if type(x)==list:
                self.coordenadas.append(x)
                break
            else:
                continue

    def buscar_posicion(eslora):
        pass