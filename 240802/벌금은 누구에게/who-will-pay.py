N, M, K = map(int, input().split())

students = [0] * (N+1)

for i in range(M):
    student = int(input())

    students[student] += 1

    if students[student] == K:
        print(student)
        break

else:
    print(-1)