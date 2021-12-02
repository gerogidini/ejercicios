#Escribir una función que calcule el área de un círculo 
#y otra que calcule el volumen de un cilindro usando la primera función.

def areaCirculo(radio):
	total = 3.14 * (radio**2)
	return total

def volumenCilindro(radio, altura):
	total = areaCirculo(radio) * altura
	return total

radioCirculo = float(input("Radio: "))
alturaCilindro = int(input("Altura: "))
print(volumenCilindro(radioCirculo, alturaCilindro))


