
class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.lst = []


    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)


    def insert_node(self, data, node):  # sourcery skip: merge-else-if-into-elif, merge-nested-ifs

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)


    def get_min(self):  # sourcery skip: assign-if-exp
        if self.root is None:
            return None
        else:
            return self.min_function(self.root)

        
    def min_function(self, node):
        # sourcery skip: assign-if-exp, reintroduce-else
        if node.left_node:
            return self.min_function(node.left_node)
        
        return node.data
    
    
    def get_max(self):  # sourcery skip: assign-if-exp
        if self.root is None:
            return None

        else:
            return self.max_function(self.root)


    def max_function(self, node):
        # sourcery skip: assign-if-exp, reintroduce-else
        if node.right_node:
            return self.max_function(node.right_node)
        
        return node.data


    def traverse(self):
        if self.root:
            self.in_order_traverse(self.root)

    
    def in_order_traverse(self, node):
        if node.left_node:
            self.in_order_traverse(node.left_node)

        print(node.data)

        if node.right_node:
            self.in_order_traverse(node.right_node)


    def get_left_side(self):  # sourcery skip: assign-if-exp
        if self.root is None:
            return None
        else:
            return self.left_side_function(self.root)


    def left_side_function(self, node):
        self.lst.append(node.data)
        if node.left_node:
            self.left_side_function(node.left_node)
        
        return self.lst

    def remove(self, data):
        if self.root is None:
            return 
        else:
            return self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if data < node.data:
            self.remove_node(data, node.left_node)

        elif data > node.data:
            self.remove_node(data, node.right_node)



if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(12)
    bst.insert(-7)
    bst.insert(186)
    bst.insert(0)
    bst.insert(-1)
    bst.insert(7)

    print(bst.get_left_side())

    # print("Max is %d:" %bst.get_max())
    # print("Min is %d:" %bst.get_min())

    # bst.traverse()







