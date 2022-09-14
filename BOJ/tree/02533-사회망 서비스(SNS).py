import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start):
    visited[start] = 1
    if len(graph[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0

    else:
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1


n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]

dfs(1)
print(min(dp[1][0], dp[1][1]))
