'''Escribir un programa que realice la devolución de una cantidad dada por el usuario en monedas.

El programa debe cumplir los siguientes requisitos:

-Solo se disponen de tres tipos de monedas: 5, 2 y 1 €. Crear una lista que contenga estos tres tipos de moneda y usar la lista en la solución.
-El programa debe preguntar al usuario por una cantidad entera de euros.
-El programa debe mostrar por pantalla el mínimo número de monedas necesarias para sumar la cantidad introducida por el usuario y cuántas monedas de cada tipo se necesitan para ello. 
 El número de monedas de cada tipo debe guardarse en otra lista.'''

monedasDisponibles = [1, 5, 2]
monedasDevueltas = [0, 0, 0]

monedasDisponibles.sort(reverse=True) #ordena la lista de mayor a menor
cantidad = int(input("Introduce valor necesitado: "))

for i in range(len(monedasDevueltas)):
	x = cantidad // monedasDisponibles[i]
	monedasDevueltas[i] = x
	cantidad = cantidad % monedasDisponibles[i]

print("Se necesitan {} monedas".format(sum(monedasDevueltas)))
for i in range(len(monedasDisponibles)):
	print(monedasDevueltas[i], "de ", monedasDisponibles[i])


	
 		