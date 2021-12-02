#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def minMultiplo(num1, num2):
	if num1 > num2:
		multiplo = num1
	else:
		multiplo = num2
	while (multiplo % num1 != 0) or (multiplo % num2 != 0):
		multiplo += 1
	return multiplo

def maxDivisor(num1, num2):
	if num1 < num2:
		divisor = num1
	else:
		divisor = num2
	while (num1 % divisor != 0) or (num2 % divisor != 0):
		divisor -=1
	return divisor

numero1 = int(input("Numero: "))
numero2 = int(input("Numero: "))

print("Minimo comun multiplo = ", minMultiplo(numero1,numero2))
print("Maximo comun divisor = ", maxDivisor(numero1,numero2))
 	