class Node:
    """Nó para a lista encadeada."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableWithLinkedLists:
    """Hash table onde cada chave aponta para uma lista encadeada."""
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        new_node = Node(key, value)
        if self.table[hashed_key] is None:
            self.table[hashed_key] = new_node
        else:
            current = self.table[hashed_key]
            while current:
                if current.key == key:
                    current.value = value  # Atualiza valor se a chave já existir
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        hashed_key = self._hash(key)
        current = self.table[hashed_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        hashed_key = self._hash(key)
        current = self.table[hashed_key]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[hashed_key] = current.next
                return True
            previous = current
            current = current.next
        return False

def menu():
    size = int(input("Informe o tamanho da hash table (lista encadeada): "))
    hash_table = HashTableWithLinkedLists(size)

    while True:
        print("\n--- Menu de Operações ---")
        print("1. Inserir elemento")
        print("2. Buscar elemento")
        print("3. Remover elemento")
        print("0. Sair")
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            key = input("Informe a chave: ")
            value = input("Informe o valor: ")
            hash_table.insert(key, value)
            print("Elemento inserido com sucesso!")
        
        elif choice == 2:
            key = input("Informe a chave para buscar: ")
            result = hash_table.get(key)
            if result is not None:
                print(f"Valor encontrado: {result}")
            else:
                print("Chave não encontrada.")
        
        elif choice == 3:
            key = input("Informe a chave para remover: ")
            if hash_table.remove(key):
                print("Elemento removido com sucesso!")
            else:
                print("Chave não encontrada.")
        
        elif choice == 0:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
