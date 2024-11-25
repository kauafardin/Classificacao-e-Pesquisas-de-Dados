class Jogo:
    def __init__(self, jogoId, titulo, desenvolvedor, preco, generos):
        # inicializa os atributos do jogo, como ID, título, desenvolvedor, preço e gêneros
        self.jogoId = jogoId
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  # lista para suportar múltiplos gêneros

class NoJogo:
    def __init__(self, jogo):
        # inicializa o nó da árvore com um jogo, sem filhos inicialmente
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        # inicializa a árvore binária de busca sem uma raiz
        self.raiz = None

    def inserir(self, jogo):
        # insere um jogo na árvore de acordo com o preço
        if self.raiz is None:
            # se a árvore estiver vazia, o jogo se torna a raiz
            self.raiz = NoJogo(jogo)
            return

        node = self.raiz
        while True:
            if jogo.preco < node.jogo.preco:
                # desce para a esquerda se o preço for menor
                if node.esquerda is None:
                    node.esquerda = NoJogo(jogo)
                    break
                node = node.esquerda
            elif jogo.preco > node.jogo.preco:
                # desce para a direita se o preço for maior
                if node.direita is None:
                    node.direita = NoJogo(jogo)
                    break
                node = node.direita
            else:
                # trata nós com preços iguais comparando títulos para manter consistência
                if jogo.titulo < node.jogo.titulo:
                    if node.esquerda is None:
                        node.esquerda = NoJogo(jogo)
                        break
                    node = node.esquerda
                else:
                    if node.direita is None:
                        node.direita = NoJogo(jogo)
                        break
                    node = node.direita

    def buscar_por_preco(self, precoUnico):
        # busca jogos com um preço específico
        resultados = []
        self._buscar_preco_aux(self.raiz, precoUnico, resultados)
        return resultados

    def _buscar_preco_aux(self, node, preco, resultados):
        # busca recursiva para encontrar jogos com um preço específico
        if node is None:
            return
        if node.jogo.preco == preco:
            resultados.append(node.jogo)
        if preco < node.jogo.preco:
            self._buscar_preco_aux(node.esquerda, preco, resultados)
        else:
            self._buscar_preco_aux(node.direita, preco, resultados)

    def buscar_por_faixa_de_preco(self, precoMinimo, precoMaximo):
        # busca jogos dentro de uma faixa de preço
        resultados = []
        self._buscar_faixa_aux(self.raiz, precoMinimo, precoMaximo, resultados)
        return resultados

    def _buscar_faixa_aux(self, node, minimo, maximo, resultados):
        # busca recursiva para encontrar jogos dentro de uma faixa de preço
        if node is None:
            return
        if minimo <= node.jogo.preco <= maximo:
            resultados.append(node.jogo)
        if minimo < node.jogo.preco:
            self._buscar_faixa_aux(node.esquerda, minimo, maximo, resultados)
        if maximo > node.jogo.preco:
            self._buscar_faixa_aux(node.direita, minimo, maximo, resultados)

class HashGeneros:
    def __init__(self):
        # inicializa a tabela hash com um dicionário
        self.generoParaJogos = {}

    def adicionar_jogo(self, jogo):
        # adiciona um jogo a cada gênero correspondente
        for genero in jogo.generos:
            if genero not in self.generoParaJogos:
                self.generoParaJogos[genero] = []
            self.generoParaJogos[genero].append(jogo)

    def obter_jogos(self, genero):
        # retorna todos os jogos associados a um gênero
        return self.generoParaJogos.get(genero, [])

#def menu():
    # função principal para interagir com o sistema
    ##arvore = ArvoreJogos()
    #hashTable = HashGeneros()
    #idsExistentes = set()  # rastreia os IDs de jogos adicionados

    #while True:
        #print("\n--- Menu de Operações ---")
        #print("1. Adicionar Jogo")
        #print("2. Buscar Jogo por preço")
        #print("3. Buscar Jogo por faixa de preço")
        #print("4. Buscar Jogo por gênero")
        #print("0. Sair")

        #opcao = input("Escolha uma opção: ").strip()

        #if opcao == "1":
            # adiciona um novo jogo
            #try:
                #jogoId = int(input("ID do jogo: "))
                #if jogoId in idsExistentes:
                    #print(f"Erro: ID {jogoId} já cadastrado.")
                    #continue
                #titulo = input("Título do jogo: ")
                #desenvolvedor = input("Nome do desenvolvedor: ")
                #preco = int(input("Preço (inteiro): R$"))
                #generos = input("Gêneros (separados por vírgula): ").split(",")
                #generos = [g.strip() for g in generos]
                #novoJogo = Jogo(jogoId, titulo, desenvolvedor, preco, generos)
                #arvore.inserir(novoJogo)
                #hashTable.adicionar_jogo(novoJogo)
                #idsExistentes.add(jogoId)
                #print(f"Jogo '{titulo}' adicionado com sucesso!")
            #except ValueError:
                #print("Erro: Insira dados válidos.")
        #elif opcao == "2":
            # busca jogos por preço exato
            #try:
                #preco = int(input("Preço: R$"))
                #resultados = arvore.buscar_por_preco(preco)
                #if resultados:
                    #for jogo in resultados:
                        #print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco}")
                #else:
                    #print(f"Nenhum jogo encontrado com preço R${preco}.")
            #except ValueError:
                #print("Erro: Insira um preço válido.")
        #elif opcao == "3":
            # busca jogos dentro de uma faixa de preço
            #try:
                #minimo = int(input("Preço mínimo: R$"))
                #maximo = int(input("Preço máximo: R$"))
                #resultados = arvore.buscar_por_faixa_de_preco(minimo, maximo)
                #if resultados:
                    #for jogo in resultados:
                        #print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco}")
                #else:
                    #print(f"Nenhum jogo encontrado na faixa de R${minimo} a R${maximo}.")
            #except ValueError:
                #print("Erro: Insira valores válidos.")
        #elif opcao == "4":
            # busca jogos por gênero
            #genero = input("Gênero: ").strip()
            #resultados = hashTable.obter_jogos(genero)
            #if resultados:
                #for jogo in resultados:
                    #print(f"Jogo encontrado: {jogo.titulo} - Gênero: {genero}")
            #else:
                #print(f"Nenhum jogo encontrado para o gênero '{genero}'.")
        #elif opcao == "0":
            #print("Saindo...")
            #break
        #else:
            #print("Opção inválida. Tente novamente.")

# Criando objetos de exemplo para inserir na árvore e na hash table
jogo1 = Jogo(1, "Jogo A", "Dev A", 50, ["Aventura", "RPG"])
jogo2 = Jogo(2, "Jogo B", "Dev B", 30, ["Estratégia", "Ação"])
jogo3 = Jogo(3, "Jogo C", "Dev C", 70, ["Aventura", "Puzzle"])
jogo4 = Jogo(4, "Jogo D", "Dev D", 30, ["Corrida"])
jogo5 = Jogo(5, "Jogo E", "Dev E", 50, ["RPG", "Ação"])

# Inicializando a árvore binária de busca e a tabela hash
arvore = ArvoreJogos()
hashTable = HashGeneros()

# Inserindo os jogos na árvore e na tabela hash
for jogo in [jogo1, jogo2, jogo3, jogo4, jogo5]:
    arvore.inserir(jogo)
    hashTable.adicionar_jogo(jogo)

# Exemplo: Busca de jogos por preço exato
print("Exemplo 1: Buscar por preço exato (R$50):")
resultados_preco = arvore.buscar_por_preco(50)
for jogo in resultados_preco:
    print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco}")

# Exemplo: Busca de jogos por faixa de preço
print("\nExemplo 2: Buscar por faixa de preço (R$30 a R$70):")
resultados_faixa = arvore.buscar_por_faixa_de_preco(30, 70)
for jogo in resultados_faixa:
    print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco}")

# Exemplo: Busca de jogos por gênero
print("\nExemplo 3: Buscar por gênero ('RPG'):")
resultados_genero = hashTable.obter_jogos("RPG")
for jogo in resultados_genero:
    print(f"Jogo encontrado: {jogo.titulo} - Gêneros: {', '.join(jogo.generos)}")

#if __name__ == "__main__":
    #menu()