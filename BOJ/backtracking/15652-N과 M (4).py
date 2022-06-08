n, m = map(int, input().split())
li = []


def dfs(start):
    if len(li) == m:
        print(' '. join(map(str, li)))
        return

    for i in range(start, n + 1):
        li.append(i)
        dfs(i)
        li.pop()


dfs(1)
