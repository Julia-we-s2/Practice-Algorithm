def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int ,input().split())
    graph.append([c, a, b])

parent = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    parent[i] = i

graph.sort()
selected = []
ans = 0

for c, a, b in graph:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += c
        selected.append(c)

ans -= selected.pop()

print(ans)
