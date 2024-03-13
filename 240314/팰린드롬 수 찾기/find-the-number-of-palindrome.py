'''
1. 두 개의 정수 X, Y가 주어진다.
2. X <= k <= Y 값 중 팰린드롬을 센다.
3. 팰린드롬은 거꾸로 읽어도 기존과 동일한 경우다.
4. 팰린드롬에 해당하는 수의 갯수를 세어라.

1- 내 풀이

1) for i in range(X, Y+1) 순회를 하며 숫자 palindrome를 특정한다.
2) 해당 수를 파싱하여 num 배열로 저장한다.
3) num 뒤에서 순회하며 앞의 Index에 저장된 수와 같으면 result += 1을 한다.
4) result를 출력한다.

'''

X, Y = map(int, input().split())

result = 0
for i in range(X, Y+1):
    num = list(map(int, str(i)))

    for check in range(len(num)):
        if num[check] != num[-(check+1)]:
            break
    
    else:
        result += 1

print(result)