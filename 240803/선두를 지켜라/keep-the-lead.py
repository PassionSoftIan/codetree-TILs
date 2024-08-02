N, M = map(int, input().split())

A = [0] * 1000001
B = [0] * 1000001

A_start = 1
B_start = 1

for i in range(N):
    v, t = map(int, input().split())

    for j in range(t):
        A[A_start + j] = A[A_start + j - 1] + v
    
    A_start += t 


for i in range(M):
    v, t = map(int, input().split())

    for j in range(t):
        B[B_start + j] = A[B_start + j - 1] + v
    
    B_start += t

count = 0
for i in range(2, 1000001):
    if A[i] == 0 or B[i] == 0:
        break
    if A[1] > B[1]:
        if A[i] < B[i]:
            count += 1
        
    elif A[1] < B[1]:
        if A[i] > B[i]:
            count += 1
    
    elif A[1] == B[1]:
        if A[i] > B[i] or A[i] < B[i]:
            count += 1

print(count)