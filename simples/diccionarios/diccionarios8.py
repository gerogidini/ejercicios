'''Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras 
y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.'''

diccionario = {}
palabras = input("Escribir palabra:traduccion y separar cada par con , : ")
lista = palabras.split(',')
for i in lista:
	clave, valor = i.split(':')
	diccionario[clave] = valor

frase = input("Frase a traducir: ")
for x in frase.split(' '):
	if x in diccionario:
		print(diccionario[x], end=' ')
	else:
		print(x) 