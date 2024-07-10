ah, am, bh, bm = map(int, input().split())

result = (bh * 60 + bm) - (ah * 60 + am)

print(result)