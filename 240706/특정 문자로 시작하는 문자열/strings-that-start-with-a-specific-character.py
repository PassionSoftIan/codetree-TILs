N = int(input())

words = []

for i in range(N):
    words.append(input())

key = input()

count = 0
len_count = 0
for word in words:
    if word[0] == key:
        count += 1
        len_count += len(word)

print(count, f"{len_count/count:.2f}")