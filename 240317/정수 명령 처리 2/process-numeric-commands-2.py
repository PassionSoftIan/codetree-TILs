from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq[0]

N = int(input())

que = Queue()
for i in range(N):
    command = list(input().split())

    if command[0] == 'push':
        que.push(int(command[1]))
    
    if command[0] == 'front':
        print(que.front())
    
    if command[0] == 'size':
        print(que.size())
    
    if command[0] == 'empty':
        if que.empty():
            print(1)
        
        else:
            print(0)
    
    if command[0] == 'pop':
        print(que.pop())