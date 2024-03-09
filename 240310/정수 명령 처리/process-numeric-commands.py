class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if self.items:
            return False
        return True
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")
    
    def top(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

N = int(input())

stack = Stack()

for i in range(N):
    line = input().split()
    method = line[0]

    if method == 'push':
        stack.push(int(line[1]))
    
    elif method == 'size':
        print(stack.size())
    
    elif method == 'empty':
        if stack.empty():
            print(1)
        else:
            print(0)
    
    elif method == 'pop':
        print(stack.pop())

    elif method == 'top':
        print(stack.top())