class HashTableWithVectors:
    """Hash table onde cada chave aponta para um vetor."""
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hashed_key]):
            if k == key:
                self.table[hashed_key][i] = (key, value)  # Atualiza valor se a chave já existir
                return
        self.table[hashed_key].append((key, value))

    def get(self, key):
        hashed_key = self._hash(key)
        for k, v in self.table[hashed_key]:
            if k == key:
                return v
        return None

    def remove(self, key):
        hashed_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hashed_key]):
            if k == key:
                del self.table[hashed_key][i]
                return True
        return False

def menu():
    size = int(input("Informe o tamanho da hash table (vetores): "))
    hash_table = HashTableWithVectors(size)

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
