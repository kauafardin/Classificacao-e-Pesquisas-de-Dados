def quick_sort(lista, inicio, fim):
    if fim > inicio:
        pivo = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, pivo-1)
        quick_sort(lista, pivo+1, fim)

def particiona(lista, inicio, fim):
    esquerda = inicio
    direita = fim
    aux = 0
    pivo = lista[inicio]
    while esquerda <= direita:
        while esquerda <= fim and lista[esquerda] <= pivo:  
            esquerda += 1
        while direita >= inicio and lista[direita] > pivo:  
            direita -= 1
        if esquerda < direita:
            aux = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = aux

    lista[inicio] = lista[direita]
    lista[direita] = pivo
    return direita
   

def teste_quick():
    lista_aleatoria = [40,20,10,80,60,50,7,30,100]
    quick_sort(lista_aleatoria, 0, len(lista_aleatoria)-1)
    print(f"Aleatória: {lista_aleatoria}")

    lista_ordenada = [7,10,20,30,40,50,60,80,100]
    quick_sort(lista_ordenada, 0, len(lista_ordenada)-1)
    print(f"Ordenada {lista_ordenada}")

    lista_inversa = [100,80,60,50,40,30,20,10,7]
    quick_sort(lista_inversa, 0, len(lista_inversa)-1)
    print(f"Inversa {lista_inversa}")

    lista_duplicada = [40,20,50,80,60,50,7,80,100]
    quick_sort(lista_duplicada, 0, len(lista_duplicada)-1)
    print(f"Duplicada {lista_duplicada}")

teste_quick()