lista =[]

def funcao_insertion_sort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1

        while(j>=0 and lista[j] > temp):
            lista[j + 1] = lista[j]
            j-=1
        
        lista[j + 1] = temp

    return print(lista)