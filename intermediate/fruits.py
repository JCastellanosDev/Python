my_fruits = {"apple", "greape", "mango"}
your_fruits = {"banana", "orange", "mango"}

all_fruits = my_fruits.union(your_fruits)#.union es para unir dos conjuntos
intersection_fruits = my_fruits.intersection(your_fruits)#.intersection es para ver los elementos en comun entre dos conjuntos
difference_fruits = my_fruits.difference(your_fruits)#.difference es para ver los elementos que estan en un conjunto pero no en otro

print()
print("All fruits:", all_fruits)
print()
print("Common fruits:", intersection_fruits)
print()
print("Fruits only in my_fruits:", difference_fruits)
print()