def heap_sort(lista, tamanho_l, pai):
    menor = pai
    filho_esquerdo = pai * 2 + 1
    filho_direito = pai * 2 + 2

    if filho_esquerdo < tamanho_l and lista[filho_esquerdo] < lista[menor]:
        menor = filho_esquerdo
    if filho_direito < tamanho_l and lista[filho_direito] < lista[menor]:
        menor = filho_direito

    if menor != pai:
        lista[pai], lista[menor] = lista[menor], lista[pai]
        heap_sort(lista, tamanho_l, menor)

def ordenar(lista):
    tamanho_l = len(lista)

    for i in range(tamanho_l // 2 - 1, -1, -1):
        heap_sort(lista, tamanho_l, i)

    for i in range(tamanho_l-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heap_sort(lista, i, 0)

    
lista_aleatória = [40,20,10,80,60,50,7,30,100]
ordenar(lista_aleatória)
print("Aleatória:", lista_aleatória)

lista_ordenada = [7,10,20,30,40,50,60,80,100]
ordenar(lista_ordenada)
print("Ordenada:", lista_ordenada)

lista_inversa = [100,80,60,50,40,30,20,10,7]
ordenar(lista_inversa)
print("Inversa:", lista_inversa)

lista_duplicada = [40,20,50,80,60,50,7,80,100]
ordenar(lista_duplicada)
print("Duplicada:", lista_duplicada)
