n = int(input())

even_count = 0
odd_count = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(n-even_count):
            print('*', end=' ')
        
        even_count += 1
    
    else:
        for j in range(odd_count):
            print('*', end=' ')
        
        odd_count += 1
    
    print()

for i in range(n):
    if i % 2 == 0:
        for j in range(even_count):
            print('*', end=' ')
        
        even_count += 1
    
    else:
        for j in range(n-odd_count):
            print('*', end=' ')
        
        odd_count += 1
    
    print()