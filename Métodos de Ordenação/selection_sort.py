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