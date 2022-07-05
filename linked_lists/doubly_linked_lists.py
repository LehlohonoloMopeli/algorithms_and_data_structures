class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    # Doubly linked lists always insert at the and
    def insert(self, data):  # sourcery skip: hoist-statement-from-if

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node


    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    
    def traverse_backwards(self):
        
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous_node


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.traverse_forward()
    print("-----------")
    linked_list.traverse_backwards()
