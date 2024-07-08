def square(N):
    count = 1

    for i in range(N):
        for j in range(N):
            print(count, end=' ')
            if count == 9:
                count = 1
            else:
                count += 1
        print()


N = int(input())

square(N)