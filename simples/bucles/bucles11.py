# una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input("Palabra: ")
for i in range(len(palabra)-1, -1, -1):
	print(palabra[i])
	