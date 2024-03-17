'''
1. N개의 숫자가 주어짐.
2. 2개의 숫자를 골라 하나의 숫자로 합침.
3. 숫자가 하나 남을 때 까지 반복.
4. 이때 a, b의 숫자가 있을 경우 합치는 비용은 a+b임.
5. 최소 비용을 구하라.

1- 내 풀이

1) 최소 값을 저장할 min_result = 0을 만든다.
2) while len(nums) != 1일 동안 while문을 반복한다.
3) nums를 역으로 정렬하여 뒤에 두 숫자를 뽑아 a, b로 만든다.
4) min_result += a+b를 한 뒤 다시 nums.append(a+b)를 한다.
5) while문이 끝나면 min_result를 출력한다.
'''

N = int(input())

nums = list(map(int, input().split()))

min_result = 0
while len(nums) != 1:
    nums.sort(reverse=True)

    a = nums.pop()
    b = nums.pop()

    min_result += a+b
    nums.append(a+b)

print(min_result)