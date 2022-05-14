import tablero as tb
import funciones as f
import time
from os import system
jugador=tb.Tablero("eep")
maquina=tb.Tablero("maq")


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

x=0
while x==0:

    ###Recojo las coordenadas del jugador y compruebo si da en el tablero de la maquina. Segun el resultado en el tablero copia del jugador se rellena con un X en caso
    ### de acertar o con una @ en caso de fallar
    
    f.mostrar_tableros(jugador.cuerpo,jugador.copia)
    f.mostrar_tableros(maquina.cuerpo,maquina.copia)
    coord=tuple(input("Introduce coordenadas de disparo--formato xy  Ejemplo x=2,y=3  ==> 23"))
    system("cls")
    dado=maquina.dado(coord)
    if dado==1:
        jugador.copia[int(coord[0]),int(coord[1])]="X"
        maquina.cuerpo[int(coord[0]),int(coord[1])]="X"
    else:
        jugador.copia[int(coord[0]),int(coord[1])]="@"
        maquina.cuerpo[int(coord[0]),int(coord[1])]="@"
    ###Dentro de este if y este else se deberia cambiar tambien el tablero de la maquina
    
    time.sleep(3)
    
    f.mostrar_tableros(jugador.cuerpo,jugador.copia)
    f.mostrar_tableros(maquina.cuerpo,maquina.copia)
    x= int(input("Salir? si==1 no==0"))
