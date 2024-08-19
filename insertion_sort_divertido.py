class Node:
    def _init_(self, number):
        self.number = number 
        self.next = None

class linked_list:
    def _init_(self):
        self.first = None

    def insertion(self, number):
        new_node = Node(number)
        if self.first is None:
            self.first = new_node
        else:
            last = self.first
            while last.next: # Percorre a lista até encontrar o último nó (com next None)
                last = last.next
            last.next = new_node

    def ordering(self, first, node):
        if first is None or first.number >= node.number:
            node.next = first
            return node
        else:
            current = first
            while current.next and current.next.number < node.number:
                current = current.next  # Encontra a posição correta para inserir o nó
            node.next = current.next
            current.next = node
        return first

    def insertion_sort(self):
        ordered_list = None
        current = self.first
        while current:
            next_node = current.next  # Guardamos a referência do próximo nó
            ordered_list = self.ordering(ordered_list, current)  # Inserimos o nó atual na lista ordenada
            current = next_node  # Passamos para o próximo nó da lista original
        self.first = ordered_list  # A lista ordenada agora é a nova lista original
    
    def print_list(self):
        current = self.first
        while current:
            print(current.number, end=" -> ")
            current = current.next
        print("None")

insertion_ordered = linked_list()
for number in [1,2,3,4,5]:
    insertion_ordered.insertion(number)

insertion_ordered.insertion_sort()
print("Lista depois da ordenação:")
insertion_ordered.print_list()

reverse_order = linked_list()
for number in [5,4,3,2,1]:
    reverse_order.insertion(number)

reverse_order.insertion_sort()
print("Lista depois da ordenação:")
reverse_order.print_list()

insertion_duplicates = linked_list()
for number in [3,4,6,3,7,5,2,7,6]:
    insertion_duplicates.insertion(number)

insertion_duplicates.insertion_sort()
print("Lista depois da ordenação:")
insertion_duplicates.print_list()


random_insertion = linked_list()
for number in [10,7,5,9,3,8,1,4,2,6]:
    random_insertion.insertion(number)

random_insertion.insertion_sort()
print("Lista depois da ordenação:")
random_insertion.print_list()