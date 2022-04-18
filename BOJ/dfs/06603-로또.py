def dfs(start, depth):
    if depth == 6:
        print(*comb)
        return

    for i in range(start, n):
        comb.append(new_li[i])
        dfs(i + 1, depth + 1)
        comb.pop()


while True:
    li = list(map(int, input().split()))
    n = li[0]
    if n == 0:
        exit()
    new_li = li[1:]
    comb = []
    dfs(0, 0)
    print()