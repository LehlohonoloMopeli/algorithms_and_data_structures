""""
What are queues:
    Abstract data type. It can be implemented either with arrays or linked lists
    It has a FIFO structure (First In First Out)
    Basic Operations are:
        enqueue()   -> Insertion operation
        dequeue()   -> Remove operation
        peek()      -> Return last item without removing it

Applications:
    Threads are stored in queues
    Important in CPU scheduling
    When data is transferred asynchronously (data not necessarily received at same 
        rate as sent) between two processes
    Graphs rely heavily on queues (breadth-first search uses queues as the underlying
    abstract data type)

"""