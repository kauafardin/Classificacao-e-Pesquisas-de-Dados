class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.left = None  
        self.right = None  

class ArvoreBinaria:
    def __init__(self):
        self.root = None  

    # Método para inserir um produto na árvore binária
    def inserir_produto(self, id, nome, descricao, preco):
        novo_produto = Produto(id, nome, descricao, preco)
        if not self.root:
            self.root = novo_produto
        else:
            atual = self.root
            while True:
                if id < atual.id:
                    if atual.left is None:
                        atual.left = novo_produto
                        break
                    atual = atual.left
                elif id > atual.id:
                    if atual.right is None:
                        atual.right = novo_produto
                        break
                    atual = atual.right
        print(f"Produto {nome} inserido com sucesso.")

    # Método para buscar um produto pelo ID
    def buscar_produto(self, id):
        atual = self.root
        while atual:
            if id == atual.id:
                return atual
            elif id < atual.id:
                atual = atual.left
            else:
                atual = atual.right
        return None

    # Método para deletar um produto pelo ID
    def deletar_produto(self, id):
        parent = None
        atual = self.root
        while atual and atual.id != id:
            parent = atual
            if id < atual.id:
                atual = atual.left
            else:
                atual = atual.right

        if atual is None:
            print("Produto não encontrado.")
            return

        # Caso 1: nó sem filhos
        if atual.left is None and atual.right is None:
            if atual != self.root:
                if parent.left == atual:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Caso 2: nó com um filho
        elif atual.left is None:
            if atual != self.root:
                if parent.left == atual:
                    parent.left = atual.right
                else:
                    parent.right = atual.right
            else:
                self.root = atual.right

        elif atual.right is None:
            if atual != self.root:
                if parent.left == atual:
                    parent.left = atual.left
                else:
                    parent.right = atual.left
            else:
                self.root = atual.left

        # Caso 3: nó com dois filhos
        else:
            sucessor = atual.right
            sucessor_parent = atual

            while sucessor.left:
                sucessor_parent = sucessor
                sucessor = sucessor.left

            if sucessor_parent != atual:
                sucessor_parent.left = sucessor.right
            else:
                sucessor_parent.right = sucessor.right

            atual.id, atual.nome, atual.descricao, atual.preco = sucessor.id, sucessor.nome, sucessor.descricao, sucessor.preco

        print(f"Produto com ID {id} deletado.")

    # Método para imprimir todos os produtos (em ordem)
    def imprimir_produtos(self):
        atual = self.root
        stack = []
        while stack or atual:
            while atual:
                stack.append(atual)
                atual = atual.left
            atual = stack.pop()
            print(f"ID: {atual.id}, Nome: {atual.nome}, Descrição: {atual.descricao}, Preço: {atual.preco}")
            atual = atual.right

def menu():
    arvore = ArvoreBinaria()

    while True:
        print("\nMenu de Operações - Árvore Binária")
        print("1. Inserir produto")
        print("2. Buscar produto")
        print("3. Deletar produto")
        print("4. Imprimir todos os produtos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = int(input("Digite o ID: "))
            nome = input("Digite o nome: ")
            descricao = input("Digite a descrição: ")
            preco = float(input("Digite o preço: "))
            arvore.inserir_produto(id, nome, descricao, preco)

        elif opcao == "2":
            id = int(input("Digite o ID do produto a ser buscado: "))
            produto = arvore.buscar_produto(id)
            if produto:
                print(f"Produto encontrado - ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}")
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            id = int(input("Digite o ID do produto a ser deletado: "))
            arvore.deletar_produto(id)

        elif opcao == "4":
            print("Produtos na árvore:")
            arvore.imprimir_produtos()

        elif opcao == "5":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    menu()
