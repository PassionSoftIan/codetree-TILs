from collections import deque

N = int(input())

deque = deque()
for i in range(N):
    command = input().split()

    c1 = command[0]

    if c1 == 'push_back':
        deque.append(int(command[1]))
    
    if c1 == 'push_front':
        deque.appendleft(int(command[1]))
    
    if c1 == 'pop_front':
        print(deque.popleft())
    
    if c1 == 'front':
        print(deque[0])

    if c1 == 'pop_back':
        print(deque.pop())

    if c1 == 'back':
        print(deque[-1])

    if c1 == 'size':
        print(len(deque))
    
    if c1 == 'empty':
        if deque:
            print(0)
        else:
            print(1)