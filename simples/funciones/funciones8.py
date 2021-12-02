#a partir de una lista crea un dict con el promedio, el mayor y el menor de esa lista.

def creaDiccionario(lista):
	diccionario = {}
	diccionario['promedio'] = sum(lista)/len(lista)
	diccionario['mayor'] = max(lista)
	diccionario['menor'] = min(lista)
	return diccionario

print(creaDiccionario([12,6,9,0,3]))
