#número entero y muestre por pantalla un triángulo rectángulo de altura el número introducido.

altura = int(input("Altura triangulo: "))
for i in range(1, altura+1):
	for x in range(i):
		print("x", end="")
	print('')

#otra forma
for i in range(altura):
	print("x" * (i+1))