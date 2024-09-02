def insertion_sort(data):
    lista = len(data)
    for j in range(1, lista):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i+1] = data[i] 
            i = i - 1
        data[i + 1] = tmp

def teste_insertion():
    data_ordenado = [1,2,3,4,5,6]
    insertion_sort(data_ordenado)
    print("Lista Ordenada", data_ordenado)

    data_reverso = [5,4,3,2,1]
    insertion_sort(data_reverso)
    print("Lista inversa", data_reverso)

    data_duplicados = [5,4,3,2,5,7,4,2,1]
    insertion_sort(data_duplicados)
    print("Lista duplicada", data_duplicados)

    data_aleatorios = [5,10,3,2,9,7,4,8,6,1]
    insertion_sort(data_aleatorios)
    print("Lista aleatória", data_aleatorios)

teste_insertion()