def bellman(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[node] != 1e9 and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n - 1:
                    return True
    return False


n, m = map(int, input().split())
edges = []
dist = [1e9 for _ in range(n + 1)]

for _ in range(m):
    a, b, time = map(int, input().split())
    edges.append((a, b, time))

negative_cycle = bellman(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])
