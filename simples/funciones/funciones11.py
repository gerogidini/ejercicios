#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y
#su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y
#devuelva una tupla con la palabra más repetida y su frecuencia.

def crearDiccionario(cadena):
	texto = cadena.split()
	diccionario = {}
	for i in texto:
		if i in diccionario:
			diccionario[i] += 1
		else:
			diccionario[i] = 1
	return diccionario

def crearTupla(diccionario):
	palabraMasRep = ''
	frecuenciaMax = 0
	for palabra, frecuencia in diccionario.items():
		if frecuencia >= frecuenciaMax:
			palabraMasRep = palabra
			frecuenciaMax = frecuencia
	return (palabraMasRep,frecuenciaMax)

frase = "hola como estas como vos ahora como estas como"
print(crearDiccionario(frase))
print(crearTupla(crearDiccionario(frase)))

