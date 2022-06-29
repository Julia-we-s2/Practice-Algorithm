import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(cur_node):
    global cnt
    visited[cur_node] = 1

    for next_node in graph[cur_node]:
        if not visited[next_node]:
            dfs(next_node)
            cnt += 1
    return cnt


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(set)
    visited = [0 for _ in range(n + 1)]
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    print(dfs(1))
