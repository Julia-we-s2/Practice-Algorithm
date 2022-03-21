n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: (x[1], x[0]))

for row in li:
    print(*row)
