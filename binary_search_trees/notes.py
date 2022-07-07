"""      
    Pre:
        Arrays and Linked lists have a common short coming, they have O(N) linear running complexity
            when it comes to searching for an arbitrary item in the data structures.
        What if the array data structure is sorted?

    Then we can use binary search trees to search for items in O(logN) logarithmic time complexity

    Defn of Tree in graph theory:
        A tree is a G(V,E) undirected graph in which any two vertices are connected by exactly one path
            or equivalently a connected acyclic undirected graph.
        We have exclusive access to the root node. Other node have to be accessed via the root node.
        Key words here are undirected and one path.

    Defn Binary Serch Trees:
        Are data structures.
        Keeps the keys in sorted order so that lookup and other operations use the principle of binary search with O(log(N)) running time
        Each node can have at most two children (left child and right child)
        Left child is smaller than parent node
        Right child is greater than parent node
        We can access root node exclusively and the rest have to be accessed via root node

        Height of the tree is the number of edges on the longest downward path bethween the root and the 
            leaf node. The number of layers 
        Number of nodes in a complete binary search tree with height h is h = log(N) + 1 = O(log(N))
        The O(log(N)) running time is valid only when the tree structure is balanced (number of nodes in subtrees
            does not differ significantly)

    Traversal:
        Means visiting every node in the binary search tree exactly once in O(N) linear running time
        Most important is the In-Order Traversal
        There exists three types:
            Pre-Order Traversal:
                We visit the root node, then the left subtree, then the right subtree in a recursive manner
            Post-Order Traversal:
                We visit the left subtree, then the right subtree, and finally the root node in a recursive manner
            In-Order Traversal (Yields the Sorted Order)
                Visit the left subtree, the root node, then the right subtree in a recursive manner

"""

