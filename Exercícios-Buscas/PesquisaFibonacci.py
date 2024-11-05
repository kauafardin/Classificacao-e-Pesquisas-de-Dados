def pesquisa_fibonacci(lista_ordenada, valor_procurado):
    tamanho_lista = len(lista_ordenada)
    fib_menos_2 = 0  # (m-2)'o Fibonacci
    fib_menos_1 = 1  # (m-1)'o Fibonacci
    fib_m = fib_menos_2 + fib_menos_1  # m' Fibonacci

    # Gera o menor Fibonacci maior ou igual ao tamanho da lista
    while fib_m < tamanho_lista:
        fib_menos_2 = fib_menos_1
        fib_menos_1 = fib_m
        fib_m = fib_menos_2 + fib_menos_1

    # Marcador para a posição de busca
    offset = -1

    # Enquanto fib_m for válido
    while fib_m > 1:
        indice = min(offset + fib_menos_2, tamanho_lista - 1)

        # Verifica o valor na posição calculada
        if lista_ordenada[indice] < valor_procurado:
            fib_m = fib_menos_1
            fib_menos_1 = fib_menos_2
            fib_menos_2 = fib_m - fib_menos_1
            offset = indice
        elif lista_ordenada[indice] > valor_procurado:
            fib_m = fib_menos_2
            fib_menos_1 -= fib_menos_2
            fib_menos_2 = fib_m - fib_menos_1
        else:
            return indice

    # Verifica o próximo item no caso do último ajuste
    if fib_menos_1 and lista_ordenada[offset + 1] == valor_procurado:
        return offset + 1

    return -1  # Retorna -1 se o valor não for encontrado

# Teste da função
resultado_fibonacci = pesquisa_fibonacci(list(range(10000)), 7890)
print("Resultado da Pesquisa Fibonacci:", resultado_fibonacci)