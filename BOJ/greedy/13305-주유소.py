n = int(input())
connection = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
m = costs[0]

for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    ans += m * connection[i]

print(ans)