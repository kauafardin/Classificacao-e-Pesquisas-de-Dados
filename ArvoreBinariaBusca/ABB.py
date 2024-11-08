class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    # Função de inserção
    def insert(self, value):
        if self.root is None:
            self.root = No(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return No(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        
        return node

    # Função de percurso pré-ordem (raiz, esquerda, direita)
    def pre_order(self, node):
        if node:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Função de percurso em ordem simétrica (esquerda, raiz, direita)
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=' ')
            self.in_order(node.right)

    # Função de percurso pós-ordem (esquerda, direita, raiz)
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=' ')

    # Função de busca
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Função de deleção
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        
        # Encontra o nó a ser deletado
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Caso 1: Nó sem filhos
            if node.left is None and node.right is None:
                return None
            # Caso 2: Nó com um filho
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Caso 3: Nó com dois filhos
            else:
                min_larger_node = self._find_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)
        
        return node

    # Função auxiliar para encontrar o menor valor em uma subárvore
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
def menu():
    arvore = ABB()

    while True:
        print("\nMenu de Operações - Árvore Binária de Busca")
        print("1. Inserir valor")
        print("2. Buscar valor")
        print("3. Deletar valor")
        print("4. Imprimir pré-ordem")
        print("5. Imprimir em ordem")
        print("6. Imprimir pós-ordem")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor a ser inserido: "))
            arvore.insert(valor)
            print(f"Valor {valor} inserido com sucesso.")
            
        elif opcao == "2":
            valor = int(input("Digite o valor a ser buscado: "))
            resultado = arvore.search(valor)
            if resultado:
                print(f"Valor {valor} encontrado na árvore.")
            else:
                print(f"Valor {valor} não encontrado.")

        elif opcao == "3":
            valor = int(input("Digite o valor a ser deletado: "))
            arvore.delete(valor)
            print(f"Valor {valor} deletado, se existia na árvore.")
            
        elif opcao == "4":
            print("Percurso Pré-ordem:")
            arvore.pre_order(arvore.root)
            print()
            
        elif opcao == "5":
            print("Percurso Em Ordem:")
            arvore.in_order(arvore.root)
            print()

        elif opcao == "6":
            print("Percurso Pós-ordem:")
            arvore.post_order(arvore.root)
            print()

        elif opcao == "7":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Chamar a função de menu para iniciar o programa
if __name__ == "__main__":
    menu()
