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

def teste_selection():
    data = [8,6,9,4,7,3,5,2,1]
    selection_sort(data)
    print("Lista Aleatória: \n",data)

    data = [1,2,3,4,5,6,7,8,9]
    selection_sort(data)
    print("Lista Ordenada: \n",data)

    data = [9,8,7,6,5,4,3,2,1]
    selection_sort(data)
    print("Lista Inversa: \n",data)

    data = [8,1,9,4,7,3,7,9,1]
    selection_sort(data)
    print("Lista Duplicados: \n",data)

teste_selection()