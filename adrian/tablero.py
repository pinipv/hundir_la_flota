import numpy as np

class Tablero:
    
    cuerpo=np.full((10,10),0)
    """Los estados para cada celda son 0==> Agua(no tocada)
                                       1==> Barco(no tocado)
                                       2==> Agua (tocada)
                                       3==> Barco(tocado)
    No se si dejaré 1 y 3. Ire a 1==>Barco y despues mirar en que barco estan esas coordenadas
     """
    
    
    def __init__(self,nombre):
        self.nombre=nombre
        
class Bote:
    """
    El estado sera None, tocado o hundido
    Times será el numero de veces que ha sido tocado
    Existirá un método para cambiar "estado" cuando se acierte en el barco y si el numero de veces que ha siod tocado == self.long se cambiara a hundido 
    """
    estado=None
    times=[0]
    """     Como idea: times contiene las veces que ha sido tocado y tuplas con las coordenadas tocadas
    """
    
    def __init__(self,long):
        self.long=long