#carga y muestra en un texto todo el diccionario.
diccionario = {}

nombre = input("Nombre: ")
edad = int(input("Edad: "))
telefono = int(input("Telefono: "))

diccionario[nombre] = nombre
diccionario[edad] = edad
diccionario[telefono] = telefono

print("{} tiene {} anos y su telefono es {}".format(diccionario[nombre], diccionario[edad], diccionario[telefono]))