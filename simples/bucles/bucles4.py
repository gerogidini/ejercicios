#pide numero y hace cuenta regresiva hasta 0

numero = int(input("Numero: "))
for i in range(numero, -1, -1):
	print(i, end=", ")