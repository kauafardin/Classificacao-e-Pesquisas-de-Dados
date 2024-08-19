def selection_sort(data):
    menor = 0
    troca = 0
    i = 0
    j = 0
    while i < len(data):
        menor = data[i]
        menor_id = i
        
        j = i + 1
        while j < len(data):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
                
            j+=1
        troca = data[i]          
        data[i] = data[menor_id] 
        data[menor_id] = troca
        i+=1

    print("Lista Ordenada: \n",data)

data = [8,6,9,4,7,3,5,2,1]
selection_sort(data)