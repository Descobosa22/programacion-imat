# Práctica 11. Objetos UBER

## Objetivo
Esta práctica pretende alcanzar los siguientes resultados de aprendizaje:
- Saber diseñar un programa con el paradigma de orientación a objetos.
- Dominar la definición de objetos mediante clases.
- Potenciar el uso de los métodos para delegar acciones en los objetos y concentrar su lógica.

## Enunciado

### Funcionalidad

Se desea desarrollar un programa que simule el comportamiento de un servicio de taxi tipo Uber. 

El programa deberá trabajar con una matriz de 5 x 5 que representará la ciudad. En ella existirán un cliente y un vehículo que se posicionarán de una forma aleatoria en la ciudad. Cuando se inicie el programa asignaremos al cliente mediante el teclado el destino al cual deberá ir, mediante unas coordenadas x, y. El formato obligatorio de entrada deberá ser "numero,numero", pudiéndo aceptarse entradas con cualquier número de espacios: 3,5 ó 3, 5 ó 3 , 5 ó 3   ,5... 

A partir de este momento el cliente comunicará al taxi su posición actual para que le pueda recoger. El taxi deberá tomar la lógica de búsqueda que considere para llegar al cliente. En el momento que el taxi llegue hasta esa posición, le indicará su destino y le dirigirá hasta él. Igualmente podrá seguir cualquier lógica.

Al llegar al destino el vehículo Uber deberá indicarle al cliente el coste del recorrido, que será igual a una cantidad fija en € por el número de celdas recorridas ( recogida del cliente + transporte al destino). El coste inicial de partida será 5€/celda, pero podrá variar en cualquier momento.

### Salida generada

La salida del programa constará de dos partes:
- Geolocalización del Uber: celdas por la que se encuentra.
- Coste al finalizar el servicio.