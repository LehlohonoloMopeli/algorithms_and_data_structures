# FIFO structure
"""
Best practise is to use doubly linked list data structure because it can manipulate 1st and last item in O(N) running time

"""
class Queue:

    def __init__(self):
        self.queue = []

    def queue_size(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []

    # O(1) linear running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time
    def dequeue(self):
        if self.queue_size() == 0:
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):  # sourcery skip: assign-if-exp, reintroduce-else
        if self.queue_size() == 0:
            return -1
        return self.queue[0]


if __name__ == '__main__':
    queue = Queue()

    for i in range(1, 4):
        queue.enqueue(i)

    print("Is queue empty: %d" % queue.is_empty())
    print("Queue size is: %d" % queue.queue_size())
    print("removing item: %d" % queue.dequeue())
    print("Last item is: %d" % queue.peek())
