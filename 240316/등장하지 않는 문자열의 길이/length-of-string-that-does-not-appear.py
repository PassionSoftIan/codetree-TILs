'''
1. 대문자 알파벳으로만 이루어진 길이가 N인 문자열이 주어짐.
2. idx가 연속적이며, arr[idx]와 arr[idx+1]의 차이가 1이라면 연속한다고 본다.
3. 몇 개 까지 2번 조건을 만족하는지에 따라 그 갯수는 길이가 된다.
4. 1부터 N까지 각 길이마다 해당 arr에서 나타나는 횟수가 2번 이상이면 통과.
5. 처음 2번 이상 나오지 않는다면 해당 길이가 min_result가 된다.
6. min_result를 출력하라.

1- 내 풀이

1) 문자열을 아스키 코드로 저장한다.
2) for i in range(N)을 순회하며 시작점(idx)을 정한다.
3) temp = [] 배열을 만든다.
4) for j in range(i, N)을 순회하며 i 부터 추가될 알파벳을 넣는다.
5) for k in range(N - len(temp))를 돌면서 temp에 저장된 배열을 확인할 시작점(check_idx)을 정한다.
6) for l in range(k, N - len(temp))을 돌면서 시작점부터 temp에 저장된 배열과 비교하여 연속인지 본다.
7) 6번 조건 충족 여부를 확인하기 위해 5와 6 사이 count를 만들고 6번 조건에 충족하면 count += 1을 한다.
8) if count == 2일 경우 result = max(result, len(temp))로 교체한다.
8) 등장하는 적이 없는 길이 중 최솟값이기 때문에 result + 1을 출력한다.

'''

N = int(input())

arr = list(map(lambda x : ord(x) - 65 , input()))

result = 0
for i in range(N):
    temp = []
    for j in range(i, N):
        temp.append(arr[j])

        count = 0
        for k in range(N - len(temp) + 1):
            for l in range(len(temp)):
                if arr[k+l] != arr[l]:
                    break
            else:
                count += 1
        if count == 2:
            result = max(result, len(temp))

print(result + 1)