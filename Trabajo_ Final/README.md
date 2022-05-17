# Hundir la flota
### Proyecto creado por Claudia, Mónica y Adrián como práctica para la parte de DataAnalytics

El juego de hundir la flota es muy popular desde hace muchos años.

En este proyecto hemos reproducido el juego en el que dos jugadores, en este caso uno de ellos la máquina, tienen posicionados 10 barcos de distintos tamaños y deben lanzar disparos al tablero del contrario para localizar sus barcos.

Este lanzamiento se realiza introduciendo dos coordenadas, primero filas y luego columnas. No es necesario dejar espacios en blanco ni marcar cualquier otro caracter para separar las coodenadas. **Ej. Fila: 4, Columna: 2 ---> marcamos 42**

Cada vez que se dispara, se busca si ahí hay un barco.

En caso de ser positivo se marca como ***Tocado*** y cuando todas las posiciones del barco han sido eliminadas, el estado será ***Hundido***.

Si no se toca el barco, el programa devuelve ***Agua***.

Gana el primero que derribe todos los barcos del contrario.

Si se desea salir del juego en cualquier momento, solo hay que marcar 'S' de Salir.

---

#### **Las librerias que se han utilizado han sido:**

+ Numpy
+ Time
+ system
+ sys

---

#### **Autores:**

+ Adrián Pinilla
+ Claudia Balderas
+ Mónica Garrido
