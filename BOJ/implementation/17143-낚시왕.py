# 1. 낚시왕이 오른쪽으로 한 칸 이동
# 2. 낚시왕이 있는 열에 있는 상어 중 땅과 제일 가까운 상어를 잡음. 잡힌 상어는 격자판에서 사라짐
# 3. 상어가 이동

# 상어가 이동하려는 칸이 격자의 경계를 넘는 경우 방향 바꿔서 속력 유지한  채 이동
# 이동 마친 후 한 칸에 상어가 두 마리 이상 있을 수 있음. 이때 큰 상어가 나머지 상어를 모두 잡아먹음
# 낚시왕이 잡은 상어 크기의 합


def fish(j): # 열은 고
    for i in range(row):
        if arr[i][j]:
            shark = arr[i][j][2]
            arr[i][j] = 0
            return shark
    return 0


def move():
    global arr
    new_arr = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if arr[i][j]:
                ni, nj, nd = get_next_location(i, j, arr[i][j][0], arr[i][j][1])

                if new_arr[ni][nj]:
                    new_arr[ni][nj] = max(new_arr[ni][nj], (arr[i][j][0], nd, arr[i][j][2]), key=lambda x: x[2])
                else:
                    new_arr[ni][nj] = (arr[i][j][0], nd, arr[i][j][2])

    arr = new_arr


def get_next_location(i, j, speed, dir):
    if dir == 1 or dir == 2:
        cycle = row * 2 - 2
        if dir == 1:
            speed += 2 * (row - 1) - i
        else:
            speed += i

        speed %= cycle

        if speed >= row:
            return 2 * row - 2 - speed, j, 1
        return speed, j, 2

    else:
        cycle = col * 2 - 2
        if dir == 4:
            speed += 2 * (col - 1) - j
        else:
            speed += j
        speed %= cycle
        if speed >= col:
            return i, 2 * col - 2 - speed, 4
        return i, speed, 3


row, col, m = map(int, input().split())
arr = [[0 for _ in range(col)] for _ in range(row)]

for _ in range(m):
    r, c, speed, dir, size = map(int, input().split())
    r, c = r - 1, c - 1
    arr[r][c] = (speed, dir, size)
    # d - 1 위/ 2 아래/ 3 오른쪽/ 4 왼쪽

ans = 0

for i in range(col):
    ans += fish(i)
    move()

print(ans)
