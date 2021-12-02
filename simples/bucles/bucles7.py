#tablas de multiplicar

for x in range(1,11):
	print("tabla del " + str(x), end=" \t")
	for i in range(1,11):
		print(x*i, end="\t")
	print("")