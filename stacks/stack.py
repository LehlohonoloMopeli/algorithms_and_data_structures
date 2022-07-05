class Stack:

    def __init__(self):
        self.stack = []

    
    def push(self, data):
        self.stack.append(data)

    
    def pop(self):

        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    
    def peek(self):  # sourcery skip: assign-if-exp, reintroduce-else
        if self.stack_size() < 1:
            return -1
            
        return self.stack[-1]

    
    def stack_size(self):
        return len(self.stack)


    def is_empty(self):
        return self.stack == []

if __name__ ==  '__main__':
    stack = Stack()

    for i in range(1, 3):
        stack.push(i)

    print("Size: %d " % stack.stack_size())
    print("Popped item: %d " % stack.pop())
    print("Popped item: %d " % stack.pop())
    print("Popped item: %d " % stack.pop())
    print("Popped item: %d " % stack.pop())
    print("Size: %d " % stack.stack_size())
    print("Is empty %d" % stack.is_empty())
    print("Last item: %d" % stack.peek())

    

