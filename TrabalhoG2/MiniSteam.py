class Jogo:
    def __init__ (self, jogoId, titulo, desenvolvedor, preco, generos):
        self.jogoId = jogoId
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos # Lista, pois um jogo pode pertencer a múltiplos gêneros

class NoJogo:
    def __init__ (self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__ (self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = NoJogo(jogo)
            return

        # Insere o jogo na árvore comparando seu preço com os nós existentes
        node = self.raiz
        while True:
            if jogo.preco < node.jogo.preco:
                # Se não houver filho à esquerda, insere o jogo
                if node.esquerda is None:
                    node.esquerda = NoJogo(jogo)
                    break
                node = node.esquerda  # Caso contrário, continua à esquerda
            elif jogo.preco > node.jogo.preco:
                # Se não houver filho à direita, insere o jogo
                if node.direita is None:
                    node.direita = NoJogo(jogo)
                    break
                node = node.direita  # Caso contrário, continua à direita
            else:
                # Se os preços forem iguais, compara os títulos
                if jogo.titulo < node.jogo.titulo:
                    # Se o título for menor, insere à esquerda
                    if node.esquerda is None:
                        node.esquerda = NoJogo(jogo)
                        break
                    node = node.esquerda  # Caso contrário, continua à esquerda
                else:
                    # Se o título for maior ou igual, insere à direita
                    if node.direita is None:
                        node.direita = NoJogo(jogo)
                        break
                    node = node.direita  # Caso contrário, continua à direita


    def buscar_por_preco(self, precoUnico):
        node = self.raiz
        resultados = []

        while node is not None:
            if node.jogo.preco == precoUnico:
                resultados.append(node.jogo)

            # Percorre a árvore para esquerda ou direita dependendo do preço
            if precoUnico < node.jogo.preco:
                node = node.esquerda
            else:
                node = node.direita

        if not resultados:
            print(f"Nenhum jogo encontrado com o preço R${precoUnico:.2f}.")
        return resultados

    def buscar_por_faixa_de_preco(self, precoMinimo, precoMaximo):
        node = self.raiz
        resultados = []

        while node is not None:
            if precoMinimo <= node.jogo.preco <= precoMaximo:
                resultados.append(node.jogo)

            if precoMinimo < node.jogo.preco:
                node = node.esquerda
            elif precoMaximo > node.jogo.preco:
                node = node.direita  
            else:
                break

        if not resultados:
            print(f"Nenhum jogo encontrado na faixa de preço de R${precoMinimo:.2f} a R${precoMaximo:.2f}.")
        return resultados
 
class HashGeneros:
    def __init__(self):
        self.generoParaJogos = {}

    def adicionar_jogo(self, jogo):
        # Adiciona o jogo aos gêneros correspondentes
        for genero in jogo.generos:
            if genero not in self.generoParaJogos:
                self.generoParaJogos[genero] = []
            self.generoParaJogos[genero].append(jogo)

    def obter_jogos(self, genero):
        # Obtém todos os jogos para um gênero específico
        if genero in self.generoParaJogos:
            return self.generoParaJogos[genero]
        else:
            return []


def menu():
    arvore = ArvoreJogos()
    hashTable = HashGeneros()
    idsExistentes = set()  # Usado para rastrear IDs de jogos já inseridos
    
    while True:
        try:
            print("\n--- Menu de Operações ---")
            print("1. Adicionar Jogo")
            print("2. Buscar Jogo por preço")
            print("3. Buscar Jogo por faixa de preço")
            print("4. Buscar Jogo por gênero")
            print("0. Sair")
            
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                try:
                    jogoId = int(input("ID do jogo: "))
                    if jogoId in idsExistentes:
                        print(f"Erro: O ID {jogoId} já foi utilizado para outro jogo. Tente novamente com um ID diferente.")
                        continue
                    
                    titulo = input("Título do jogo: ")
                    desenvolvedor = input("Nome do Desenvolvedor: ")
                    preco = float(input("Preço: R$"))
                    generos = input("Gêneros (separados por vírgulas): ").split(",")
                    generos = [g.strip() for g in generos]
                    
                    novoJogo = Jogo(jogoId, titulo, desenvolvedor, preco, generos)
                    
                    arvore.inserir(novoJogo)
                    hashTable.adicionar_jogo(novoJogo)
                    idsExistentes.add(jogoId)
                    
                    print(f"Jogo '{titulo}' inserido com sucesso!")
                except ValueError:
                    print("Erro: Dados inválidos. Certifique-se de inserir números onde solicitado.")
            
            elif opcao == 2:
                try:
                    preco = float(input("Preço: R$"))
                    resultados = arvore.buscar_por_preco(preco)
                    for jogo in resultados:
                        print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco:.2f}")
                except ValueError:
                    print("Erro: O preço deve ser um número válido.")
            
            elif opcao == 3:
                try:
                    precoMin = float(input("Preço mínimo: R$"))
                    precoMax = float(input("Preço máximo: R$"))
                    resultados = arvore.buscar_por_faixa_de_preco(precoMin, precoMax)
                    for jogo in resultados:
                        print(f"Jogo encontrado: {jogo.titulo} - R${jogo.preco:.2f}")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos para os preços.")
            
            elif opcao == 4:
                genero = input("Gênero: ").strip()
                resultados = hashTable.obter_jogos(genero)
                if resultados:
                    for jogo in resultados:
                        print(f"Jogo encontrado: {jogo.titulo} - Gênero: {genero}")
                else:
                    print(f"Nenhum jogo encontrado no gênero '{genero}'.")
            
            elif opcao == 0:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Digite uma opção válida.")


if __name__ == "__main__":
    menu()