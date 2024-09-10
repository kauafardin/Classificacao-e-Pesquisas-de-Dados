def heap_sort(lista, tamanho, i):
    maior = i
    esquerdo = 2 * i + 1
    direito = 2 * i + 2

    if esquerdo < tamanho and lista[esquerdo] < lista[maior]:
        maior = esquerdo
    if direito < tamanho and lista[direito] < lista[maior]:
        maior = direito
    
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heap_sort(lista, tamanho, maior)

def ordenar(lista):
    tamanho = len(lista)

    for i in range(tamanho // 2 - 1, -1, -1):
        heap_sort(lista, tamanho, i)

    for i in range(tamanho-1, 0, -1):
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

