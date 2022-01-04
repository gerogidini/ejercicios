#a partir de n hace la suma de los numeros desde uno a n. Lo hago de 2 maneras. 1 con for y la otra con n(n+1)/2

n=int(input("Ingrese numero: "))
suma = 0
for i in range(1, (n+1)):
	print(i)
	suma += i
print(suma)

suma2 = (n * (n+1))/2
print(suma2)'''	






