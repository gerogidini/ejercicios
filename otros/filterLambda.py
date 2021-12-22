#utilizando FILTER y LAMBDA devuelve los menores de edad.

class Alumno:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def __str__(self):
		return "{} tiene {} anos".format(self.nombre, self.edad)

listaAlumnos = [

Alumno("Juan", 18),
Alumno("Ivan", 12),
Alumno("Ana", 19),
Alumno("Pipo", 14)

]

mayores = filter(lambda alumno:alumno.edad >= 18, listaAlumnos)

for mayor in mayores:
	print(mayor)