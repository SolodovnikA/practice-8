n = int(input())
for i in range(2, n+1):
    k = 0
    for j in range(1, i+1):
        if i % j == 0:
            k += 1
    if k == 2:
        print(i)
