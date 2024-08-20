def merge_sort(lista, inicio, fim):

    for i in range(len(lista)):
        if inicio < fim:
            meio = (inicio + fim)//2
            merge_sort(lista, inicio, meio)
            merge_sort(lista, meio+1, fim)
            merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):

    temporario = []
    fim1 = 0
    fim2 = 0
    p1 = inicio
    p2 = meio + 1
    
    for i in range(fim - inicio + 1):
        if fim1 == 0 and fim2 == 0:
            if lista[p1] <= lista[p2]:
                temporario.append(lista[p1] )
                p1 += 1
                if p1 > meio:
                    fim1 = 1
            else:
                temporario.append(lista[p2] )
                p2 += 1
                if p2 > fim:
                    fim2 = 1
                
        elif fim1 == 0:
            temporario.append(lista[p1])
            p1 += 1
            if p1 > meio:
                fim1 = 1
        else:
            temporario.append(lista[p2])
            p2 += 1
            if p2 > fim:
                fim2 = 1
        
    i += 1
                       
    for j in range (len(temporario)):
        lista[inicio + j] = temporario[j]

lista = [3,4,5,2,1,6]
merge_sort(lista, 0, len(lista)-1)
print(lista)

