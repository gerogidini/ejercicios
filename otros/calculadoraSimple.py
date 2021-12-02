print("CALCULADORA\n")

print("Menu de opciones\n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Exponente\n")

numero = int(input("Ingrese numero de operacion: "))
if numero == 1:
    numero = float(input("Ingrese primer valor: "))
    numero += float(input("Ingrese segundo valor: "))
elif numero == 2:
    numero = float(input("Ingrese primer valor: "))
    numero -= float(input("Ingrese segundo valor: "))
elif numero == 3:
    numero = float(input("Ingrese primer valor: "))
    numero *= float(input("Ingrese segundo valor: "))
elif numero == 4:
    numero = float(input("Ingrese primer valor: "))
    numero /= float(input("Ingrese segundo valor: "))
elif numero == 5:
    numero = float(input("Ingrese primer valor: "))
    numero **= float(input("Ingrese segundo valor: "))
else:
    print("Opcion invalida.")
    numero = 0

print("El resultado es ",numero)

print("\nEnd of program.")

