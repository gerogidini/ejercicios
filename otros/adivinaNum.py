#Juego de adivinar el numero.

import random

class Juego:
	def __init__(self, minimo, maximo):
		self.minimo = minimo
		self.maximo = maximo
		self.intentos = 5

	def numeroAleatorio(self):
		return random.randint(self.minimo, self.maximo)

	def inicio(self):
		print("BIENVENIDO AL JUEGO")
		print("Tendras 5 intentos para adivinar el numero oculto entre {} y {}".format(self.minimo,self.maximo))
		numero_oculto = self.numeroAleatorio()
		while self.intentos > 0:
			numero_jugador = int(input("Ingrese numero: "))
			if numero_jugador == numero_oculto:
				print("GANASTE!! Adivinaste el numero!!!")
				break
			elif numero_jugador < numero_oculto:
				print("Fallaste. El numero oculto es mayor")
			elif numero_jugador > numero_oculto:
				print("Fallaste. El numero oculto es menor")	
			self.intentos -= 1
		if self.intentos == 0:
			print("Perdiste. Se te acabaron los intentos. El numero era el " + str(numero_oculto))
			

jugar = Juego(1, 10)
jugar.inicio()


