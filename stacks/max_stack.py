"""
Question: 
    Get the maximum of a stack using O(1) linear time and O(N) memory complexity

Solution:
    As you are creating the main stack, create max stack as well that takes large values only

"""

class MaxStack:
    
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    
    def push(self, data):
        self.main_stack.append(data)

        if self.stack_size() == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    
    def get_max_item(self):
        return self.max_stack[-1]

    
    def stack_size(self):
        return len(self.main_stack)


   

if __name__ ==  '__main__':
    stack = MaxStack()
    
    stack.push(15)
    stack.push(4)
    stack.push(87)
    stack.push(12)

    print("Maximum item is: %d" % stack.get_max_item())
    
