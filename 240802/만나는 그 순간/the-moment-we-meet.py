N, M = map(int, input().split())

A = [0] * 10000
B = [0] * 10000

start_A = 1
for i in range(N):
    d, t = map(str, input().split())
    t = int(t)

    if d == 'R':
        for j in range(start_A, start_A + t):
            A[j] = A[j-1] + 1
    
    else:
        for j in range(start_A, start_A + t):
            A[j] = A[j-1] - 1
    
    start_A = start_A + t

start_B = 1
for i in range(M):
    d, t = map(str, input().split())
    t = int(t)

    if d == 'R':
        for j in range(start_B, start_B + t):
            B[j] = B[j-1] + 1
    
    else:
        for j in range(start_B, start_B + t):
            B[j] = B[j-1] - 1
    
    start_B = start_B + t

for i in range(1, 1001):
    if A[i] == B[i] and A[i] != 0 and B[i] != 0:
        print(i)
        break

else:
    print(-1)