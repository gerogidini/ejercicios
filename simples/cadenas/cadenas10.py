'''productos de una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta.'''

productos = input("Productos: ")
print(productos.replace(',', '\n'))

print('\n'.join(productos.split(','))) 
'''join devuelve una cadedna (a partir de una lista, productos.split() es la lista en este caso), 
separada x el primer parametro (/n en este caso)'''