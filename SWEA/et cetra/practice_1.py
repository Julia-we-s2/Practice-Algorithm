t = int(input())

for tc in range(t):

    n = int(input())
    cnt = 0
    info = [list(map(int, input().split())) for _ in range(3)]
    li = []
    order = [
        (info[0], info[1], info[2]), (info[0], info[2], info[1]),
        (info[1], info[0], info[2]), (info[1], info[2], info[0]),
        (info[2], info[0], info[1]), (info[2], info[1], info[0])
    ]
 
    for p in order:
        visited = [1] + [0 for _ in range(n)]

        for i in p:
            fishing = i[0]
            people = i[1]

            for j in range(0, n):
                if people <= 0:
                    break

                if visited[fishing - j] == 0:
                    people -= 1
                    visited[fishing - j] = 1
                    cnt += (j + 1)

                if people > 0 and j != 0 and fishing + j <= n and visited[fishing + j] == 0:
                        people -= 1
                        visited[fishing + j] = 1
                        cnt += (j + 1)

        li.append(cnt)
        cnt = 0

        visited = [1] + [0 for _ in range(n)]

        for i in p:
            fishing = i[0]
            people = i[1]

            for j in range(0, n):
                if people <= 0:
                    break

                if people > 0 and j != 0 and fishing + j <= n and visited[fishing + j] == 0:
                    people -= 1
                    visited[fishing + j] = 1
                    cnt += (j + 1)

                if people > 0 and visited[fishing - j] == 0:
                    people -= 1
                    visited[fishing - j] = 1
                    cnt += (j + 1)

        li.append(cnt)
        cnt = 0

    ans = min(li)
    print(f'#{tc+1} {ans}')

