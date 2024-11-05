import math

def jump_search(lista, valor_procurado):
    tamanho_lista = len(lista)
    jumps = int(math.sqrt(tamanho_lista))     
    indice = 0

    # Realiza saltos até que o valor no índice seja maior ou igual ao valor procurado ou saia do limite
    while indice < tamanho_lista and lista[min(indice, tamanho_lista - 1)] < valor_procurado:
        # Salva o índice do bloco anterior
        ultimo_indice = indice
        indice += jumps
        if indice >= tamanho_lista:
            return "Valor não encontrado"
    
    # Busca linear dentro do bloco encontrado
    for i in range(ultimo_indice, min(indice, tamanho_lista)):
        if lista[i] == valor_procurado:
            print(f"Índice: {i}\nValor: {valor_procurado}")
            return

    print("Valor não encontrado")

l_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valor = 6
jump_search(l_ordenada, valor)
