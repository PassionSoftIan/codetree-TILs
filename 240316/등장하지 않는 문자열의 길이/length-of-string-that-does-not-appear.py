'''
1. 대문자 알파벳으로만 이루어진 길이가 N인 문자열이 주어짐.
2. idx가 연속적이며, arr[idx]와 arr[idx+1]의 차이가 1이라면 연속한다고 본다.
3. 몇 개 까지 2번 조건을 만족하는지에 따라 그 갯수는 길이가 된다.
4. 1부터 N까지 각 길이마다 해당 arr에서 나타나는 횟수가 2번 이상이면 통과.
5. 처음 2번 이상 나오지 않는다면 해당 길이가 min_result가 된다.
6. min_result를 출력하라.

1- 내 풀이

1) 문자열을 아스키 코드로 저장한다.
2) for i in range(1, N//2 + 1) 무조건 2번 이상 등장을 해야하니 idx는 절반만 가져가며 길이는 1 이상이다.
3) 2번을 순회하며 길이를 특정한다.
4) 
'''

N = int(input())

arr = list(map(lambda x : ord(x) - 65 , input()))

result = N//2 + 1
for i in range(1, N//2 + 1):
    bit = 0
    for j in range(N//2 + 1):
        for k in range(1, i-1):
            if arr[j+k] - arr[j+k-1] != 1:
                break
        else:
            bit = 1
    if bit == 0:
        print(i)
        exit()

print(result)