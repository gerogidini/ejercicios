#Devuelve TRUE o FALSE si una cadena es palindromo o no. 

def palindromo(sentencia):
	sentencia = sentencia.lower().replace(' ', '')
	reversa = sentencia[::-1]
	return sentencia == reversa

sentencia = input("Sentencia: ")
print(palindromo(sentencia))
