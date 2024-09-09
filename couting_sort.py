def counting_sort(lista):    
    # Determine o valor mínimo e máximo
    minimo = min(lista)
    maximo = max(lista)
    
    # Vetor de contagem
    count = [0] * (maximo - minimo + 1)
    
    # Preencha o vetor de contagem
    for i in lista:
        count[i - minimo] += 1

    # Construa o vetor ordenado
    ordenado = []
    for i, cnt in enumerate(count):
        ordenado.extend([i + minimo] * cnt)
    
    return ordenado

lista_aleatória = [3, 2, 4, 8, 3, 1, 7, 9, 5]
print("Aleatória:", counting_sort(lista_aleatória))

lista_ordenada = [1, 2, 2, 4, 5, 5, 7, 8, 9]
print("Ordenada:", counting_sort(lista_ordenada))

lista_inversa = [9, 8, 7, 6, 5, 3, 3, 2, 1]
print("Inversa:", counting_sort(lista_inversa))

lista_duplicada = [3, 2, 4, 4, 1, 5, 6, 5, 1]
print("Duplicada:", counting_sort(lista_duplicada))
