from collections import deque


def bfs(start, end):
    cnt = 0
    queue = deque()
    queue.append((start, cnt))
    visited[start] = 1

    while queue:
        x, cnt = queue.popleft()
        if x == end:
            return cnt
        
        # cnt += 1
        for i in relation[x]:
            if visited[i] == 0:
                queue.append((i, cnt + 1))
                visited[i] = 1
    return -1


n = int(input())

p1, p2 = map(int, input().split())

m = int(input())

relation = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

print(bfs(p1, p2))