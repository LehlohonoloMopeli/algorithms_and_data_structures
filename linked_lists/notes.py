"""
    Notes on linked lists:
        1. A linked list is a data structure that consists of a group of nodes
        2. Each node in a linked list contains data and a pointer to the next node
        3. The last node in a linked list does not have a pointer to the next node
        4. Linked lists need more memory than arrays because they store data and references to other nodes
        5. The first node in a linked list is called the head node
        6. The last node in a linked list is called the tail node
        7. Finding an arbitrary item in a linked list is O(n) linear time
        
    Advantages:
        1. Linked lists can store different sized items (arrays can only store fixed-size items)
        2. Linked lists are dynamic data structures, they can acquire memory at runtime by inserting new nodes
        3. Access the first node exclusively
        4. It cannot have holes in the data so there is no need to shift items around
        5. Items are not stored next to each other in memory so there is no random indexing
        6. Linked lists allow us to create more complex data structures such as stacks and queues
        7. inserting items at the beginning of the data structure is O(1)
        8. Deleting an item at the beginning of the data structure is O(1)
        9. Inserting or removing an item in an arbritrary or last position is O(n) because we have to start from the 
            first node and search until we find it

    Disadvantages:
        1. Linked lists are not as fast as arrays because they have to traverse the entire list to find an item
        2. Need more memory because of references to other nodes
        3. There is no random access to items in a linked list
        4. Cannot go backwards in a linked list (cannot access a previous node)
        5. Not predictable - the running time of the application depends on the operations by the user

"""
