max_len = 0
min_len = 21

for i in range(3):
    check = len(input())
    if check > max_len:
        max_len = check
    
    if check < min_len:
        min_len = check
print(max_len - min_len)