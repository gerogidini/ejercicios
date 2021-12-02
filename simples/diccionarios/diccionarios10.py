'''Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Terminar.'''

clientes = {}
terminar = False
while terminar == False:
	opcion = int(input("1-Anadir  2-Eliminar  3-Mostrar Cliente  4-Listar Clientes  5-Terminar. "))
	if opcion == 1:
		codigo = int(input("Ingrese ID: "))
		nombre = input("Nombre: ")
		telefono = int(input("Telefono: "))
		cliente = {'nombre':nombre, 'telefono':telefono}
		clientes[codigo] = cliente
	if opcion == 2:
		codigo = int(input("Ingrese codigo de cliente a eliminar"))
		del clientes[codigo]
	if opcion == 3:
		codigo = int(input("Ingrese codigo de cliente a mostrar"))
		if codigo in clientes:
			print(clientes[codigo])
	if opcion == 4:
		for cliente in clientes:
			print(cliente.value())
	if opcion == 5:
		print("CHAUUUUU")
		terminar = True