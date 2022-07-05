"""
 Question 7: Given a standard linked list, find the middle node without using extra memory.

 Solution: Using two pointers. 
        First Pointer: Traverse the linked list one node at a time.
        Second Pointer: Traverse the list two nodes at a time

        When the faster pointer reaches the end of the list, the slower pointer
        will be in the middle node


Question 8: Given a standard Linked List, reverse it in-place (do not use more memory)

"""



class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0


    def size_of_list(self):
        return self.number_of_nodes


    def insert_at_beginning(self, data):
        self.number_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next_node = None
        else:
            new_node.next_node = self.head
            self.head = new_node


    def insert_at_end(self, data):
        self.number_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next_node = None
        else:
            actual_node = self.head

            # This while loop is what causes the O(N) linear time complexity
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node


    def remove_node(self, data):
        if self.head is None:
            return 

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data is not data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # Missed search, data does not exist
        if actual_node is None:
            return

        # If the previous node is still none, then the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # Remove internal node
            # No need to delete this node, garbage collection will take care of it
            previous_node.next_node = actual_node.next_node


    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer


    def reverse(self):

        current_node = self.head
        next_node = None
        previous_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


    # Loop through the linked list
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node
            
    
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(6)
    linked_list.insert_at_beginning(32)
    linked_list.insert_at_beginning(65)
    linked_list.insert_at_beginning(11)
    linked_list.insert_at_beginning(2)
    linked_list.traverse()
    print("==================")
    print("Reversed List: ")
    linked_list.reverse()
    linked_list.traverse()

