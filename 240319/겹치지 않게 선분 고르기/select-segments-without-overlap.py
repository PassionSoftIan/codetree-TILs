'''
1. 수직선이 있다.
2. N개의 선분이 주어진다.
3. 겹치지 않게 가장 많은 수의 선분을 고르라.
4. 단, 끝점을 공유해도 겹친 것이다.


1- 내 풀이

1) 수직선을 나타낼 배열을 만든다. line = [0] * 1001
2) 모든 선분의 조합을 다 구해본다.
3) 해당 조합의 선분을 일직선위에 그려보고 겹치는 경우에는 해당 조합의 개수를 최대 개수로 늘리지 않는다.
4) max_result를 출력한다.


'''


def find_combination(depth):
    global max_result

    if max_result == N:
        return

    if depth > N:
        return

    if depth <= N:
        the_line = [0] * 1001
        for line in lines:
            x1, x2 = line_segments[line]
            for draw in range(x1, x2+1):
                if the_line[draw] != 1:
                    the_line[draw] = 1
                else:
                    return

        max_result = max(max_result, depth)


    for i in range(N):
        lines.append(i)
        find_combination(depth + 1)
        lines.pop()



N = int(input())

line_segments = [list(map(int, input().split())) for _ in range(N)]

max_result = -1

lines = []

find_combination(0)

print(max_result)