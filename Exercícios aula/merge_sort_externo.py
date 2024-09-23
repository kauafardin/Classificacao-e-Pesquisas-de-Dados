import random
import os
import heapq  # Usado para mesclar os arquivos ordenados eficientemente

# Função para criar um arquivo com números aleatórios
def criar_arquivo(nome):
    with open(nome, "w") as arquivo:
        for i in range(1000):
            arquivo.write(f"{random.randint(1, 1000)}\n")


# Função para criar arquivos ordenados a partir do arquivo principal
def criar_arquivo_ordenado(nome):
    print(f"Criando arquivos temporários ordenados a partir de {nome}...")
    vetor = []
    contador = 0
    max_linhas_por_arquivo = 100  # Limite de linhas para cada arquivo temporário

    # Abrindo o arquivo original para leitura
    with open(nome, "r") as arquivo:
        for linha in arquivo:
            vetor.append(float(linha.strip()))  # Convertendo cada linha em float
            # Quando atingir o limite de linhas, cria um arquivo temporário
            if len(vetor) >= max_linhas_por_arquivo:
                contador += 1
                vetor.sort()
                nome_temp = f"Temp{contador}.txt"
                with open(nome_temp, "w") as temp_arquivo:
                    for num in vetor:
                        temp_arquivo.write(f"{num}\n")
                print(f"Arquivo temporário {nome_temp} criado e ordenado.")
                vetor.clear()  # Limpa o vetor para armazenar mais linhas

        # Se restarem linhas no vetor após a leitura, cria mais um arquivo temporário
        if vetor:
            contador += 1
            vetor.sort()
            nome_temp = f"Temp{contador}.txt"
            with open(nome_temp, "w") as temp_arquivo:
                for num in vetor:
                    temp_arquivo.write(f"{num}\n")
            print(f"Arquivo temporário {nome_temp} criado e ordenado.")

    # Retorna o número de arquivos temporários criados
    return contador


# Função para mesclar arquivos (merge)
def merge(nome_final, k, t):
    print(f"Mesclando {k} arquivos temporários em {nome_final}...")
    
    arquivos_temporarios = [open(f"Temp{i+1}.txt", "r") for i in range(k)]
    with open(nome_final, "w") as arquivo_final:
        # Usando heapq para mesclar os arquivos de forma eficiente
        heap = []
        
        # Inicializando o heap com o primeiro número de cada arquivo
        for i, arquivo in enumerate(arquivos_temporarios):
            linha = arquivo.readline().strip()
            if linha:
                heapq.heappush(heap, (float(linha), i))
        
        # Continuar retirando o menor valor do heap e adicionando ao arquivo final
        while heap:
            menor, index = heapq.heappop(heap)
            arquivo_final.write(f"{menor}\n")
            # Ler a próxima linha do arquivo de onde o menor valor foi retirado
            linha = arquivos_temporarios[index].readline().strip()
            if linha:
                heapq.heappush(heap, (float(linha), index))
    
    # Fechando todos os arquivos temporários
    for arquivo in arquivos_temporarios:
        arquivo.close()

    print(f"Merge finalizado. Arquivo {nome_final} criado.")


# Função para remover arquivos temporários
def remove(nome):
    if os.path.exists(nome):
        os.remove(nome)
        print(f"Arquivo {nome} removido.")
    else:
        print(f"Arquivo {nome} não encontrado.")


# Função principal de merge sort externo
def merge_sort_externo(nome):
    n = 1000  # Número total de registros
    k = criar_arquivo_ordenado(nome)  # Simula a criação dos arquivos temporários e retorna a quantidade
    t = n // (k + 1)  # Calcula o valor de t
    print(f"Número de arquivos: {k}")
    print(f"Valor de t: {t}")

    # Nome do arquivo final
    nome_final = "dados_ordenados.txt"

    # Mescla os arquivos temporários
    merge(nome_final, k, t)

    # Remove arquivos temporários após o merge
    for i in range(k):
        novo = f"Temp{i+1}.txt"
        remove(novo)


def main():
    nome_arquivo = "dados.txt"
    criar_arquivo(nome_arquivo)
    merge_sort_externo(nome_arquivo)


if __name__ == "__main__":
    main()
