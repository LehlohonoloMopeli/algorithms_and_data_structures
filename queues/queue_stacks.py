"""
The aim is to design a queue abstract data type with the help of stacks.

"""

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)


    def dequeue(self):  # sourcery skip: raise-specific-error

        if len(self.enqueue_stack) == len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty")  

        if len(self.dequeue_stack) == 0:

            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            
        return self.dequeue_stack.pop()  


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(34)
    queue.enqueue(1)
    queue.enqueue(7564)

    print(queue.dequeue())

    queue.enqueue(111)

    print(queue.dequeue())



