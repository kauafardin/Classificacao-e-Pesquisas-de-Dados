def bolha(lista):
    for j in range(len(lista)):
        for i in range(j+1,len(lista)):
            if lista[i] < lista[j]:
                troca = lista[j]
                lista[j] = lista[i]
                lista[i] = troca
    print(lista)

lista = [5,1,3,4,2]
bolha(lista)

lista = [5,4,3,2,1]
bolha(lista)

lista = [1,2,3,4,5]
bolha(lista)
