#Elimina vocales de cadena

cadena = input("Ingrese frase: ")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
texto_nuevo = ""

for x in cadena:
	if x not in vocales:
		texto_nuevo += x

print(texto_nuevo)