def union(x, y):
    global i, ans
    x = find(x)
    y = find(y)

    if x == y:
        ans = i + 1
    else:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


ans = 0
n, m = map(int, input().split())
parents = [i for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    if not ans:
        union(x, y)

print(ans)
