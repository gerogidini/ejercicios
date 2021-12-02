#muestra la cantidad de veces q aparece cada vocal en una palabra

word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
  print("La vocal " + vocal + " aparece " + str(word.count(vocal)) + " veces")