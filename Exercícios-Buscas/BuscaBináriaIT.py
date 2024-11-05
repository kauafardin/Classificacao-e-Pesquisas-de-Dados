def busca_binaria_iterativa(lista_ordenada, valor_procurado):
    indice_inicio = 0
    indice_fim = len(lista_ordenada) - 1

    # Enquanto a janela de busca estiver válida
    while indice_inicio <= indice_fim:
        indice_meio = (indice_inicio + indice_fim) // 2

        # Verifica se o valor está no meio da janela atual
        if lista_ordenada[indice_meio] == valor_procurado:
            return indice_meio
        # Se o valor do meio for menor, ajusta o índice de início
        elif lista_ordenada[indice_meio] < valor_procurado:
            indice_inicio = indice_meio + 1
        # Se o valor do meio for maior, ajusta o índice de fim
        else:
            indice_fim = indice_meio - 1

    return -1  # Retorna -1 se o valor não for encontrado

# Teste da função
resultado_iterativo = busca_binaria_iterativa(list(range(10000)), 7890)
print("Resultado da Busca Binária Iterativa:", resultado_iterativo)