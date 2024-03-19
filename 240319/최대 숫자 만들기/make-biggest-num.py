from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return -1
    
    if x + y < y + x:
        return 1
    
    return 0

N = int(input())

nums = [input() for _ in range(N)]

nums.sort(key=cmp_to_key(compare))

print(*nums, sep='')