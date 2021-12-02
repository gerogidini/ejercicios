#Diccionario con facturas sin pagar, se puede agregar o paga.

diccionario = {123:100}
total_pagado = 0
terminar = False
while terminar == False:
	opcion = int(input("1 - Anadir  2 - Pagar  3 - Terminar "))
	if opcion == 1:
		clave = int(input("Ingrese numero de factura: "))
		valor = int(input("Ingrese valor de factura: "))
		diccionario[clave] = valor
	elif opcion == 2:
		print(diccionario.keys())
		clave = int(input("Ingrese numero de factura a pagar: "))
		total_pagado += diccionario[clave]
		del diccionario[clave]
	elif opcion == 3:
		terminar = True
		print("Chau....se cobraron ${} y falta cobrar ${}".format(total_pagado, sum(diccionario.values())))