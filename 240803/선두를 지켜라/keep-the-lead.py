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
        B[B_start + j] = B[B_start + j - 1] + v
    
    B_start += t

count = 0
A_check = 0
B_check = 0

check = 1
while True:
    if A[check] > B[check] or A[check] < B[check]:
        A_check = A[check]
        B_check = B[check]
        break
    check += 1
print()

for i in range(2, 1000001):
    if A[i] == 0 or B[i] == 0:
        break
    if A_check > B_check:
        if A[i] < B[i]:
            count += 1
            A_check = A[i]
            B_check = B[i]
        
    elif A_check < B_check:
        if A[i] > B[i]:
            count += 1
            A_check = A[i]
            B_check = B[i]

    elif A_check == B_check:
        if A[i] > B[i] or A[i] < B[i]:
            count += 1
            A_check = A[i]
            B_check = B[i]

print(count)