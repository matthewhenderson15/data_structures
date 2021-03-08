class myStack:
    # Subclass for definining parent child relationship of stack members
    class StackNode:
        def __init__(self, val, child):
            self.val = val
            self.child = child
    
    # Define class members
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
    
    # Define primary operations for stack
    def pop(self):
        if self.is_empty():
            return('Stack is empty')
        temp = self.head.val
        self.head = self.head.child
        self.size -= 1
        return temp

    def push(self, x):
        newNode = self.StackNode(x, self.head)
        self.head = newNode
        self.size += 1
    
    def top(self):
        if self.is_empty():
            return('Stack is empty')
        return self.head.val
    
    def stack_size(self):
        return self.size
    
    def is_empty(self):
        return self.stack_size() == 0

test_instance = myStack()
test_instance.push(1)
print(test_instance.top())
print(test_instance.is_empty())
test_instance.push(2)
print(test_instance.top())
test_instance.pop()
print(test_instance.top())
test_instance.pop()
print(test_instance.is_empty())
print(test_instance.top())
# 1 False 2 1 True 'Stack is empty'