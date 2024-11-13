lista = []

def funcao_bubble_sort(lista):
    for i in range (len(lista)):
        troca = False
        for j in range (0, len(lista) - i -1):
            if lista[j] > lista[j + 1]:
                variavel_reserva = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = variavel_reserva
                troca = True
        if troca == False:
            break

    return print(lista)