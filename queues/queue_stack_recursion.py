"""
Problem: Implement a queue using stacks but recursively with one stack

"""

class Queue:
    def __init__(self):
        self.stack = []


    def enqueue(self, data):
        self.stack.append(data)

    # The items stay in memory so there are two stacks in practise but you did not define it
    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()

        self.stack.append(item)

        return dequeued_item


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(3)
    queue.enqueue(54)
    queue.enqueue(311)
    queue.enqueue(908)

    print(queue.dequeue())

    queue.enqueue(1111)

    print(queue.dequeue())


