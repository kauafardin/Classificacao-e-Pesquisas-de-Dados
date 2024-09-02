def shell_sort(lista):
    sublist = len(lista)//2
    while sublist > 0:
        for posicao_inicial in range(sublist):
            ordenando(lista, posicao_inicial, sublist)
        print(f"Após incrementos de tamanho {sublist} a lista é {lista}")

        sublist = sublist//2

def ordenando(lista, inicio, intervalo):
    for i in range(inicio+intervalo, len(lista), intervalo):
        valor_atual = lista[i]
        posicao = i

        while posicao >= intervalo and lista[posicao-intervalo] > valor_atual:
            lista[posicao] = lista[posicao-intervalo]
            posicao = posicao - intervalo
        lista[posicao] = valor_atual

lista_aleatoria = [40,20,10,80,60,50,7,30,100]
shell_sort(lista_aleatoria)
print(f"Aleatória: {lista_aleatoria}")

lista_ordenada = [7,10,20,30,40,50,60,80,100]
shell_sort(lista_ordenada)
print(f"Ordenada {lista_ordenada}")

lista_inversa = [100,80,60,50,40,30,20,10,7]
shell_sort(lista_inversa)
print(f"Inversa {lista_inversa}")

lista_duplicada = [40,20,50,80,60,50,7,80,100]
shell_sort(lista_duplicada)
print(f"Duplicada {lista_duplicada}")