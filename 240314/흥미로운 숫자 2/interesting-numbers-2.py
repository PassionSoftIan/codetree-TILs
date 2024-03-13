'''
1. 숫자 X, Y가 주어진다.
2. X <= Y 중 흥미로운 숫자가 있다.
3. 흥미로운 숫자는 한 자리 빼고 모든 자릿수 숫자가 같다.
4. 흥미로운 숫자의 개수는 몇 개인가.

1- 내 풀이
1) range(X, Y+1) 순회를 한다.
2) 순회를 하며 숫자를 각 자리수 별로 분리한다.
3) 0~9까지 있는 num_check 배열을 만든다.
3) 분리된 숫자 배열을 순회하며 num_check에 있는 자기 번호에 +=1 한다
4) num_check 배열을 순회하며 index 값이 1인 숫자가 하나 것과 0보다 이상인 숫자가 하나만 있는지 체크한다.
5) 4번 조건을 충족하면 result += 1한다.
6) result를 출력한다.
'''

X, Y = map(int, input().split())

result = 0
for i in range(X, Y+1):
    num_check = [0] * 10
    nums = list(map(int, str(i)))

    for j in range(len(nums)):
        check_num = nums[j]
        num_check[check_num] += 1
    
    check_1 = 0
    check_else = 0
    for check in num_check:
        if check == 1:
            check_1 += 1
        elif check > 0:
            check_else += 1
    
    if check_1 == 1 and check_else == 1:
        result += 1
print(result)