def busca_binaria_recursiva(lista_ordenada, valor_procurado, indice_inicio=0, indice_fim=None):
    if indice_fim is None:
        indice_fim = len(lista_ordenada) - 1

    # Caso base: se os limites cruzarem, o valor não está na lista
    if indice_inicio > indice_fim:
        return -1

    indice_meio = (indice_inicio + indice_fim) // 2

    # Verifica se o valor está no meio
    if lista_ordenada[indice_meio] == valor_procurado:
        return indice_meio
    # Se o valor do meio for menor, ajusta a busca para a metade direita
    elif lista_ordenada[indice_meio] < valor_procurado:
        return busca_binaria_recursiva(lista_ordenada, valor_procurado, indice_meio + 1, indice_fim)
    # Se o valor do meio for maior, ajusta a busca para a metade esquerda
    else:
        return busca_binaria_recursiva(lista_ordenada, valor_procurado, indice_inicio, indice_meio - 1)

# Teste da função
resultado_recursivo = busca_binaria_recursiva(list(range(10000)), 7890)
print("Resultado da Busca Binária Recursiva:", resultado_recursivo)