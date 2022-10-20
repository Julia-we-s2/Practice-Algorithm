n, m = map(int, input().split())
trains = [[0 for _ in range(20)] for _ in range(n)]
cnt = 0
check_trains = set()

for _ in range(m):
    command = list(map(int, input().split()))

    if command[0] == 1:
        i = command[1]
        x = command[2]
        if not trains[i - 1][x - 1]:
            trains[i - 1][x - 1] = 1
    elif command[0] == 2:
        i = command[1]
        x = command[2]
        if trains[i - 1][x - 1]:
            trains[i - 1][x - 1] = 0
    elif command[0] == 3:
        i = command[1]
        trains[i - 1][-1] = 0
        for j in range(18, -1, -1):
            trains[i - 1][j + 1] = trains[i - 1][j]
            trains[i - 1][j] = 0
    else:
        i = command[1]
        trains[i - 1][0] = 0
        for j in range(1, 20):
            trains[i - 1][j - 1] = trains[i - 1][j]
            trains[i - 1][j] = 0

for i in range(n):
    string_train = ''.join(map(str, trains[i]))
    if string_train not in check_trains:
        cnt += 1
    check_trains.add(string_train)

print(cnt)