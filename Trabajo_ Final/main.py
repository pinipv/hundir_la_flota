import utils as ut
import time
from os import system
import numpy as np
import sys

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

time.sleep(2)

system("cls")

z= ''

while z != "s":

    '''Se inician los tableros de la maquina y el del usuario tras solicitar el nombre de jugador'''
    
    Jugador_persona = ut.Tablero(input("Escribe tu nombre: ")) 
    Jugador_maquina = ut.Tablero("Maquina")

    '''Para inciar el juego declaramos una variable igual a "0" que será la que provoque que el juego continue hasta que el usuario decida salir '''

    x = '0'

    '''Comienza el juego el jugador. Cada vez que acabe el turno, esta variable será actualizada con el oponente'''

    turno_jugador = "Persona"

    while x != '1':
        system("cls")
        try:

            '''Cuando comienza el juego e inicia la persona, se imprimen los tableros con los barcos colocados de forma aleatoria.
                Se le solicita unas coordenadas al jugador que se transformarán en tupla.
                estas coordenadas se comprobaran si corresponden a una posición de un barco en el tablero de la máquina y,
                en caso de ser correcto, se reescribirá con una X si no hay barco se reescribe con @ (agua)'''

            if turno_jugador == "Persona" : 
                Jugador_persona.imprimir_tableros_juego()
                print()
                coord = tuple(input("Si desea salir pulse 'S' o Introduzca coordenadas de disparo->  Ej: fila = 2, columna = 3  ==> 23: "))
                if coord[0] == 's' or coord[0] =='S':
                    print('\n', '¡Gracias por jugar!', '\n')
                    time.sleep(1)
                    sys.exit()
                
                coord = (int(coord[0]),int(coord[1]))

                dado = Jugador_maquina.dado(coord)   #comprobamos en el tablero del oponente "maquina", si hemos dado a alguno de los barcos con las coordenada introducidas
                if dado == 0:
                    Jugador_persona.tablero_disparo[coord[0],coord[1]] = "@"     #actualizo el tablero si he dado agua "@"
                    turno_jugador = "Maquina"
        
                elif dado == 1:
                    Jugador_persona.tablero_disparo[coord[0],coord[1]] = "X"     #actualizo el tablero si he dado disparo "X"
        
                elif dado == 2:
                    print('\n', 'Coordenada errónea', '\n')

                else:
                    Jugador_persona.tablero_disparo[coord[0],coord[1]] = "X"     #para pintar el último disparo en mi tablero
                    system("cls")
                    Jugador_persona.terminar_partida(Jugador_maquina)
                    break

                '''Cuando el turno corresponde a la maquina, las coordenadas de disparo se ponen aleatorias.
                Al igual que en el tablero de la persona, si da con un barco del jugador se reescribe con X y si no con @ (agua)'''
                
                time.sleep(1)
            else:
                coord= np.random.randint(10, size = 2)
                coord = (int(coord[0]),int(coord[1]))
            
                dado= Jugador_persona.dado(coord)   #comprobamos en el tablero del oponente "persona", si hemos dado a alguno de los barcos con las coordenada introducidas
                if dado == 0:
                    Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "@"     #actualizo el tablero si he dado agua "@"
                    turno_jugador = "Persona"
        
                elif dado == 1:
                    Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "X"     #actualizo el tablero si he dado disparo "X"
        
                elif dado == 2:
                    print('\n', 'Coordenada errónea', '\n')
            
                else:
                    Jugador_maquina.tablero_disparo[coord[0],coord[1]]= "X"     #para pintar el último disparo en la máquina del jugador
                    system("cls")
                    Jugador_maquina.terminar_partida(Jugador_persona)
                    break
        except Exception as e:
            print('\nHa habido un error en las coordenadas introducidas')
            time.sleep(1.5)
    
    print('\n', '¡Gracias por jugar!', '\n')
    
    z = input('Si desea salir pulse "S": ')
    system("cls")
print("¡Hasta pronto!", '\n')