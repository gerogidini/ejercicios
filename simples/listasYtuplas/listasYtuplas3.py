#una lista con materias y la otra se va completando con las notas
materias = ["Lengua", "Historia", "Fisica"]
notas = []

for materia in materias:
	nota = input("Nota de " + materia + ": ")
	notas.append(nota)

for i in range(len(materias)):
	print("En {} sacaste {}".format(materias[i], notas[i]))