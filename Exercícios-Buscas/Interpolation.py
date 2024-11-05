def interpolation(lista, valor_procurado):
    ini = 0
    fim = len(lista) - 1

    # Enquanto a janela de busca estiver válida
    while ini <= fim:
        meio = ini + ((fim - ini) * (valor_procurado - lista[ini])) / (lista[fim] - lista[ini])

        # Verifica se o valor está no meio da janela atual
        if lista[meio] == valor_procurado:
            return meio
        # Se o valor do meio for menor, ajusta o índice de início
        elif lista[meio] < valor_procurado:
            ini = meio + 1
        # Se o valor do meio for maior, ajusta o índice de fim
        else:
            fim = meio - 1

    return -1  # Retorna -1 se o valor não for encontrado

# Teste da função
lista_ordenada= [2, 4, 6, 8, 10, 12, 14, 16]
chave = int(input("Número: "))
resultado = interpolation(lista_ordenada, chave)
print("Resultado da Busca Binária Iterativa:", resultado)