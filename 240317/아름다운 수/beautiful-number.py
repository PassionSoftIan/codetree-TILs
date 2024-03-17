'''
1. 1 <= 4 숫자로 이루어져 있는 세상이다.
2. 1은 1개 2는 2개 ... 연달아서 나오는 숫자가 아름다운 숫자다.
3. 연달아 나오는 묶음이 여러개여도 상관없다.
4. 예를 들어 111 은 1이 한 개 나온게 3 묶음 있는 것.
5. 2222 는 2가 2개 나온 묶음이 2개.
6. 222 는 2가 2개 나온 묶음이 1개이며 2 하나는 묶음이 될 수 없기에 아름다운 수가 아니다.
7. 다만, 122와 같은 경우에는 아름다운 수의 묶음으로만 이루어져 있기 때문에 아름다운 수로 간주한다.
8. N개의 자리수가 주어졌을 경우 아름다운 수의 묶음으로만 이루어진 숫자가 몇 개 나올 수 있는지 구하라.

'''


def find_beautiful_num(depth):
    global result

    if depth == N:       

        for num in range(1, 5):
            count = 0
            for check in range(N):
                if nums[check] == num:
                    count += 1
                else:
                    if count % num != 0:
                        return
                    else:
                        count = 0
                
            if count != 0 and count % num != 0:
                return
        
        result += 1
        return
    
    for i in range(1, 5):
        nums.append(i)
        find_beautiful_num(depth+1)
        nums.pop()


N = int(input())

nums = []

result = 0

find_beautiful_num(0)

print(result)