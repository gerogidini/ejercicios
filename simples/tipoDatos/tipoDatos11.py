#Ingresa un valor y calcula el 4% de interes de 3 años

plata = float(input("Ingrese valor: "))
interes = 1.04
ano1 = plata * interes
ano2 = ano1 * interes
ano3 = ano2 * interes

print("1er ano {} - 2do ano {} - 3er ano {}".format(round(ano1, 2), ano2 , round(ano3, 2)))
