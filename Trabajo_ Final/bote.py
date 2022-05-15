class Bote:
                                                           ### contiene tuplas con coordenadas del barco
    
                                                                ### veces tocado 
    
    def __init__(self,eslora,tablero):
        self.estado=None
        self.coordenadas=[]
        self.veces=[0]
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
        
    