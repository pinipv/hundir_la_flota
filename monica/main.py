import utils as ut
import constants as cs
import time
from os import system
import numpy as np

print("""
                                                                                              
,-----.   ,--.                                              ,--.    ,--.                      
|  |) /_  `--'  ,---.  ,--,--,  ,--.  ,--.  ,---.  ,--,--,  `--'  ,-|  |  ,---.       ,--,--. 
|  .-.  \ ,--. | .-. : |      \  \  `'  /  | .-. : |      \ ,--. ' .-. | | .-. |     ' ,-.  | 
|  '--' / |  | \   --. |  ||  |   \    /   \   --. |  ||  | |  | \ `-' | ' '-' '     \ '-'  | 
`------'  `--'  `----' `--''--'    `--'     `----' `--''--' `--'  `---'   `---'       `--`--' 
                                                                                             
                                                                                                              
,--.                           ,--. ,--.             ,--.               ,---. ,--.           ,--.            
|  ,---.  ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |  ,--,--.     /  .-' |  |  ,---.  ,-'  '-.  ,--,--. 
|  .-.  | |  ||  | |      \ ' .-. | ,--. |  .--'     |  | ' ,-.  |     |  `-, |  | | .-. | '-.  .-' ' ,-.  | 
|  | |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  | \ '-'  |     |  .-' |  | ' '-' '   |  |   \ '-'  | 
`--' `--'  `----'  `--''--'  `---'  `--' `--'        `--'  `--`--'     `--'   `--'  `---'    `--'    `--`--'                                                                                                                                                                                                                                                                                                   
          """)
time.sleep(3)
system("cls")

Jugador_persona = ut.Tablero(input("Escribe tu nombre: ")) 
Jugador_maquina = ut.Tablero("Maquina")

x=0

turno_jugador= "Persona"   #El primer turno corresponde a la persona. Cada vez que acabe el turno, esta variable será actualizada con el oponente   

while x==0:
    system("cls")

    if turno_jugador == "Persona" : 
        Jugador_persona.imprimir_tableros_juego()
        coord=tuple(input("Introduce coordenadas de disparo--formato xy  Ejemplo x=2,y=3  ==> 23 : "))
        coord= (int(coord[0]),int(coord[1]))

        dado= Jugador_maquina.dado(coord)   #comprobamos en el tablero del oponente "maquina", si hemos dado a alguno de los barcos con las coordenada introducidas
        if dado == 0:
            Jugador_persona.tablero_disparo[coord[0],coord[1]]= "@"     #actualizo el tablero si he dado agua "@"
            turno_jugador = "Maquina"
       
        elif dado == 1:
            Jugador_persona.tablero_disparo[coord[0],coord[1]]= "X"     #actualizo el tablero si he dado disparo "X"
      
        else:
            Jugador_persona.tablero_disparo[coord[0],coord[1]]= "X"     #para pintar el último disparo en mi tablero
            system("cls")
            Jugador_persona.terminar_partida(Jugador_maquina)
           
    else:
        Jugador_maquina.imprimir_tableros_juego()
        coord= np.random.randint(10, size = 2)
        
        dado= Jugador_persona.dado(coord)   #comprobamos en el tablero del oponente "persona", si hemos dado a alguno de los barcos con las coordenada introducidas
        if dado == 0:
            Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "@"     #actualizo el tablero si he dado agua "@"
            turno_jugador = "Persona"
       
        elif dado == 1:
            Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "X"     #actualizo el tablero si he dado disparo "X"
      
        else:
            Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "X"     #para pintar el último disparo en la máquina del jugador
            system("cls")
            Jugador_maquina.terminar_partida(Jugador_persona)

    x= int(input("Salir? si == 1 no == 0 : "))