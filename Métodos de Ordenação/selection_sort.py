lista = []

def funcao_selection_sort(lista):
    for i in range(len(lista) - 1):
        min = i;

        for j in range(i+1, len(lista)):
            if(lista[min] > lista[j]):
                min = j

        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
    
    return print(lista)


import random
from random import randint
random.seed(0)

array =[]

for i in range(1, 100):
    x = randint(1, 1000)
    print(x)
    array.append(x)

print("Selection:")
funcao_selection_sort(array)