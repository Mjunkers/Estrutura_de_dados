def funcao_merge_sort(lista):
    if len(lista) <= 1:
        return

    # Dividindo a lista ao meio (duas partes)
    middle = len(lista) // 2
    left_lista = lista[:middle]
    right_lista = lista[middle:]

    # chamada recursiva para ordenar as duas metades
    funcao_merge_sort(left_lista)
    funcao_merge_sort(right_lista)

    # juntando as duas partes ordenadas
    merge(left_lista, right_lista, lista)


def merge(left_lista, right_lista, lista):
    i = 0  # Índice da lista final
    l = 0  # Índice da lista da esquerda
    r = 0  # Índice da lista da direita

    # Comparando elementos das listas left_lista e right_lista
    while l < len(left_lista) and r < len(right_lista):
        if left_lista[l] < right_lista[r]:
            lista[i] = left_lista[l]
            l += 1
        else:
            lista[i] = right_lista[r]
            r += 1
        i += 1

    # Adicionando elementos restantes na left_lista
    while l < len(left_lista):
        lista[i] = left_lista[l]
        l += 1
        i += 1

    # Adicionando elementos restantes na right_lista
    while r < len(right_lista):
        lista[i] = right_lista[r]
        r += 1
        i += 1

import random
from random import randint

random.seed(0)

array = []

for i in range(1, 100):
    x = randint(1, 1000)
    array.append(x)

print("Array original:")
print(array)

print("\nMerge Sort:")
funcao_merge_sort(array)
print("\nArray ordenado:")
print(array)
