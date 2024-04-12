count = int(input())
summ = 0
ans = []

for i in range(count + 1):
  summ += i
  ans.append(summ)

for i in range(len(ans)+1):
    print(ans[i-1])