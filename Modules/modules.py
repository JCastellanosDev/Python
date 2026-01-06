import random #importar la libreria random para generar numeros aleatorios

dice = [1, 2, 3, 4, 5, 6] #definir un dado de 6 caras

print(random.choices(dice, k=3)) #la k sirve para especificar cuantas veces quiero que tire el dado