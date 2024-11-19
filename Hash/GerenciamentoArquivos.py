class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome       
        self.caminho = caminho  
        self.tamanho = tamanho  
        self.tamanho = None  # Corrigido para evitar sobrescrever o atributo

class Gerenciamento:
    def __init__(self, tamanhoLista):
        self.tamanhoLista = tamanhoLista 
        # Cria uma tabela hash vazia onde cada posição é inicialmente None
        self.tabela = {i: None for i in range(tamanhoLista)}

    # Método privado que calcula o índice hash com base no nome do arquivo
    def _hash(self, nome):
        # Retorna o índice da tabela com base no hash do nome
        return hash(nome) % self.tamanhoLista

    # Método para inserir um novo arquivo na tabela hash
    def inserir(self, nome, caminho, tamanho):
        hash_nome = self._hash(nome)
        novo_arquivo = Arquivo(nome, caminho, tamanho)
        
        # Se a posição na tabela está vazia, insere o novo arquivo diretamente
        if self.tabela[hash_nome] is None:
            self.tabela[hash_nome] = novo_arquivo
        else:
            # Caso contrário, trata colisão usando lista encadeada
            atual = self.tabela[hash_nome]
            while atual:
                # Se já existe um arquivo com o mesmo nome, atualiza o caminho e o tamanho
                if atual.nome == nome:
                    atual.caminho = caminho  # Atualiza o caminho
                    atual.tamanho = tamanho  # Atualiza o tamanho
                    return
                # Se não há próximo nó, sai do laço para adicionar o novo arquivo
                if atual.tamanho is None:
                    break
                # Move para o próximo nó
                atual = atual.tamanho
            # Adiciona o novo arquivo na lista encadeada
            atual.tamanho = novo_arquivo

    # Método para buscar um arquivo na tabela hash
    def obter(self, nome):
        # Calcula o índice hash para localizar o arquivo
        hash_nome = self._hash(nome)
        # Começa a busca a partir do primeiro elemento na lista encadeada
        atual = self.tabela[hash_nome]
        
        # Percorre a lista encadeada
        while atual:
            # Se o nome do arquivo for encontrado, retorna o caminho
            if atual.nome == nome:
                return atual.caminho
            # Move para o próximo nó
            atual = atual.tamanho
        # Retorna None se o arquivo não for encontrado
        return None

    # Método para remover um arquivo da tabela hash
    def remover(self, nome):
        # Calcula o índice hash para localizar o arquivo
        hash_nome = self._hash(nome)
        atual = self.tabela[hash_nome]
        anterior = None  # Variável para manter o nó anterior
        
        # Percorre a lista encadeada
        while atual:
            # Se o nome do arquivo for encontrado, remove-o
            if atual.nome == nome:
                # Se existe um nó anterior, ele aponta para o próximo nó
                if anterior:
                    anterior.tamanho = atual.tamanho
                else:
                    # Caso contrário, a tabela aponta para o próximo nó
                    self.tabela[hash_nome] = atual.tamanho
                return True  # Indica que o arquivo foi removido
            # Atualiza o nó anterior e move para o próximo
            anterior = atual
            atual = atual.tamanho
        # Retorna False se o arquivo não for encontrado
        return False
    
    # Método para listar todos os arquivos na tabela hash
    def listar(self):
        print("\n--- Listagem de Arquivos ---")
        for idx, arquivo in self.tabela.items():
            if arquivo is not None:  # Verifica se há arquivos na posição da tabela
                atual = arquivo
                while atual:  # Enquanto houver mais arquivos na lista encadeada
                    print(f"Nome: {atual.nome}, Caminho: {atual.caminho}, Tamanho: {atual.tamanho}")
                    atual = atual.tamanho  # Move para o próximo arquivo na lista encadeada

# Função para exibir o menu e interagir com o usuário
def menu():
    # Solicita o tamanho da tabela hash ao usuário
    tamanho = int(input("Informe o tamanho da tabela hash (lista encadeada): "))
    # Cria uma instância da classe Gerenciamento
    gerenciamento = Gerenciamento(tamanho)

    # Loop do menu até o usuário escolher sair
    while True:
        # Exibe as opções do menu
        print("\n--- Menu de Operações ---")
        print("1. Inserir elemento")
        print("2. Buscar elemento")
        print("3. Remover elemento")
        print("4. Listar")
        print("0. Sair")
        # Solicita uma opção do usuário
        opcao = int(input("Escolha uma opção: "))

        # Inserção de um novo arquivo
        if opcao == 1:
            nome = input("Informe o nome do arquivo: ")
            caminho = input("Informe o caminho do arquivo: ")
            tamanho = int(input("Informe o tamanho do arquivo: "))
            gerenciamento.inserir(nome, caminho, tamanho)
            print("Elemento inserido com sucesso!")
        
        # Busca por um arquivo
        elif opcao == 2:
            nome = input("Informe o nome do arquivo para buscar: ")
            resultado = gerenciamento.obter(nome)
            if resultado is not None:
                print(f"Caminho encontrado: {resultado}")
            else:
                print("Arquivo não encontrado.")
        
        # Remoção de um arquivo
        elif opcao == 3:
            nome = input("Informe o nome do arquivo para remover: ")
            if gerenciamento.remover(nome):
                print("Elemento removido com sucesso!")
            else:
                print("Arquivo não encontrado.")
        
        # Listagem de todos os arquivos
        elif opcao == 4:
            gerenciamento.listar()
            
        # Opção para sair do programa
        elif opcao == 0:
            print("Saindo do programa.")
            break
        
        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa com o menu principal
if __name__ == "__main__":
    menu()
