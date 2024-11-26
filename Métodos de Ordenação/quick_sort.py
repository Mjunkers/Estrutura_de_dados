def funcao_quick_sort(lista):
    # Caso base: listas com tamanho 1 ou vazio já estão ordenadas
    if len(lista) <= 1:
        return lista

    # Escolhendo o pivô (usaremos o último elemento da lista)
    pivot = lista[-1]
    left_lista = []  # Elementos menores que o pivô
    right_lista = []  # Elementos maiores ou iguais ao pivô

    # Particionando a lista em duas partes
    for i in range(len(lista) - 1):  # Ignorando o pivô
        if lista[i] < pivot:
            left_lista.append(lista[i])
        else:
            right_lista.append(lista[i])

    # Chamadas recursivas e concatenando o resultado
    sorted_left = funcao_quick_sort(left_lista)
    sorted_right = funcao_quick_sort(right_lista)
    return sorted_left + [pivot] + sorted_right


# Testando o código com um array gerado aleatoriamente
import random
from random import randint

random.seed(0)

array = []

# Gerando valores aleatórios para a lista
for i in range(1, 100):
    x = randint(1, 1000)
    array.append(x)

print("Array original:")
print(array)

print("\nQuick Sort:")
sorted_array = funcao_quick_sort(array)
print("\nArray ordenado:")
print(sorted_array)
