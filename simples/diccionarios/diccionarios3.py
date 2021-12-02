#diccionario con fruta-precio pregunta x una fruta y una cantidad y devuelve el costo

diccionario = {'Manzana': 1.30, 'Pera': 2.01, 'Banana': 1.65}

fruta = input("Que fruta?: ")
cantidad = int(input("Cuanta?: "))

if fruta in diccionario:
	print("{} kilos de {} cuestan {}".format(cantidad, fruta, diccionario[fruta]*cantidad))
else:
	print("No hay de eso")

print(sum(diccionario.values()))