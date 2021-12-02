#carga palabras en una lista mientras se ponga 's'

cargar = "s"
lista = []
while cargar == "s":
	materia = input("Materia: ")
	lista.append(materia)
	cargar = input("Seguir cargando? ")
print(lista)
