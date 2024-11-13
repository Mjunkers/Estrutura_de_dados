import random
from random import randint
random.seed(0)

from bubble_sort import funcao_bubble_sort
from insertion_sort import funcao_insertion_sort
from selection_sort import funcao_selection_sort

array = []

for i in range(1, 100):
    x = randint(1, 1000)
    print(x)
    array.append(x)

print("\nBubble:")
funcao_bubble_sort(array)

print("\nInsertion:")
funcao_insertion_sort(array)

print("\nSelection:")
funcao_selection_sort(array)