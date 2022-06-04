import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    nums[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if nums[i] == 0:
                nums[i] = -nums[a]
                queue.append(i)
            else:
                if nums[i] == nums[a]:
                    return False
    return True


k = int(input())

for tc in range(k):
    vertex, edge = map(int, input().split())
    isTrue = True

    graph = [[] for _ in range(vertex + 1)]
    nums = [0 for _ in range(vertex + 1)]

    for _ in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, vertex + 1):
        if nums[i] == 0:
            if not bfs(i):
                isTrue = False
                break
    print("YES" if isTrue else "NO")