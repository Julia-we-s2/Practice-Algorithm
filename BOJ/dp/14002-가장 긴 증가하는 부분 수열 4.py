# 아 대박~  앞에서부터 출력하면 안 되는구나!!!

n = int(input())
li = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

temp = []
order = max(dp)

for i in range(n - 1, -1, -1):
    if dp[i] == order:
        temp.append(li[i])
        order -= 1

for num in temp[::-1]:
    print(num, end=' ')
