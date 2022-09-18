
def dfs(no, fishing, people, distance, visited):
    global answer
    isVisited = False
    if people == 0:
        if no != 2:
            no += 1
            dfs(no, p[no][0], p[no][1], distance, visited)
        else:
            answer = min(answer, distance)
        return
    for j in range(n):
        if fishing + j <= n and visited[fishing + j] == 0:
            visited[fishing + j] = 1
            dfs(no, fishing, people - 1, distance + (j + 1), visited)
            visited[fishing + j] = 0
            isVisited = True

        if fishing - j >= 0 and visited[fishing - j] == 0:
            visited[fishing - j] = 1
            dfs(no, fishing, people - 1, distance + (j + 1), visited)
            visited[fishing - j] = 0
            isVisited = True

        if isVisited:
           break


for tc in range(int(input())):
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(3)]
    answer = float('inf')
    order = [
        (info[0], info[1], info[2]), (info[0], info[2], info[1]),
        (info[1], info[0], info[2]), (info[1], info[2], info[0]),
        (info[2], info[0], info[1]), (info[2], info[1], info[0])
    ]
    for p in order:
        dfs(0, p[0][0], p[0][1], 0, [1] + [0 for _ in range(n)])

    print(f'#{tc+1} {answer}')

