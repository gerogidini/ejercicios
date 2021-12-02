#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(num):
	resultado = 1
	for i in range(num, 0, -1):
		resultado *= i
	return resultado

numero = int(input("Numero: "))
print(factorial(numero))