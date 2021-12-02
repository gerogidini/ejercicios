#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados(lista):
	otraLista = []
	for i in lista:
		otraLista.append(i**2)
	return otraLista

print(cuadrados([1,2,4,5]))