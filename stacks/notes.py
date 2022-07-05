""""
What are stacks:
    Abstract data type. It can be implemented either with arrays or linked lists
    It has a LIFO structure (Last In First Out)
    Basic operations are:
        pop()   -> Used to remove last item
        push()  -> Used to insert item in last place
        peek()  -> Used to view last item without removing it
    Most modern programming languages are stack-oriented
    They define most basic operations such as adding two numbers

Applications:
    In stack-oriented programming languages
    Graph algorithms rely heavily on stacks such as depth-first search
    Back button in web browsers (recently visited websites and urls are pushed
        onto a stack and the back button pops these urls)
    Undo operations in softwares (Such as VS code)

Memory Management:
    There are two main types of memory: stack memory and heap memory
    Stack Memory (Implemented with the stack data structure):
        Is a special region in the RAM
        Small in size
        Fast access
        Stores the active functions and local variables
        This is how python knows where to return after finishing execution of a function
    Heap Memory (Not implemented with the heap data structure):
        Is a special region in the RAM
        Size of a heap memory is way larger than that of a stack memory (we can store more items)
        Slow access
        Stores objects
        
"""
