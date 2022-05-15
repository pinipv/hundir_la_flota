import utils as ut
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

'''Se inician los tableros de la maquina y el del usuario tras solicitar el nombre de jugador'''

Jugador_persona = ut.Tablero(input("Escribe tu nombre: ")) 
Jugador_maquina = ut.Tablero("Maquina")

'''Para inciar el juego declaramos una variable igual a 0 que será la que provoque que el juego continue hasta que el usuario decida salir '''

x = 0

'''Comienza el juego el jugador. Cada vez que acabe el turno, esta variable será actualizada con el oponente'''

turno_jugador = "Persona"

while x == 0:
    system("cls")
    '''Cuando comienza el juego e inicia la persona, se imprimen los tableros con los barcos colocados de forma aleatoria.
        Se le solicita unas coordenadas al jugador que se transformarán en tupla.
        estas coordenadas se comprobaran si corresponden a una posición de un barco en el tablero de la máquina y,
        en caso de ser correcto, se reescribirá con una X si no hay barco se reescribe con @ (agua)'''
    if turno_jugador == "Persona" : 
        Jugador_persona.imprimir_tableros_juego()
        print()
        coord = tuple(input("Introduce coordenadas de disparo--formato xy  Ejemplo x=2,y=3  ==> 23 : "))
        coord = (int(coord[0]),int(coord[1]))

        dado = Jugador_maquina.dado(coord)   #comprobamos en el tablero del oponente "maquina", si hemos dado a alguno de los barcos con las coordenada introducidas
        if dado == 0:
            Jugador_persona.tablero_disparo[coord[0],coord[1]] = "@"     #actualizo el tablero si he dado agua "@"
            turno_jugador = "Maquina"
       
        elif dado == 1:
            Jugador_persona.tablero_disparo[coord[0],coord[1]] = "X"     #actualizo el tablero si he dado disparo "X"
      
        else:
            Jugador_persona.tablero_disparo[coord[0],coord[1]] = "X"     #para pintar el último disparo en mi tablero
            system("cls")
            Jugador_persona.terminar_partida(Jugador_maquina)

        '''Cuando el turno corresponde a la maquina, las coordenadas de disparo se ponen aleatorias.
        Al igual que en el tablero de la persona, si da con un barco del jugador se reescribe con X y si no con @ (agua)'''

        x= int(input("¿Desea salir del juego? Si= 1 No = 0 : "))

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

print('¡Gracias por jugar!')