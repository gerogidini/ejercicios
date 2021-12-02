#imprime un triangulo rectangulo con numeros de dos en dos.

numero = int(input("Numero: "))
if numero % 2 == 0:
	for i in range(0, numero+1, 2):
		for x in range(i, -1, -2):
			print(x, end=" ")
		print("")
else:
	for i in range(1, numero+1, 2):
		for x in range(i, 0, -2):
			print(x, end=" ")
		print("")