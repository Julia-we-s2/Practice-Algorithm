import sys
input = sys.stdin.readline


def check(team):
    global ans
    another_team = set()
    team_cnt = 0
    another_team_cnt = 0

    for i in range(n):
        if i not in team:
            another_team.add(i)

    for i in team:
        for j in team:
            if i != j:
                team_cnt += arr[i][j]

    for i in another_team:
        for j in another_team:
            if i != j:
                another_team_cnt += arr[i][j]

    ans = min(ans, abs(another_team_cnt - team_cnt))


def dfs(start, team):
    if len(team) == n // 2:
        check(team)
        return

    for i in range(start, n):
        dfs(i + 1, team | {i})


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
dfs(0, set())
print(ans)
