def check_row(r, num):
    for c in range(9):
        if boards[r][c] == num:
            return False
    return True


def check_col(c, num):
    for r in range(9):
        if boards[r][c] == num:
            return False
    return True


def check_square(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if boards[nr + i][nc + j] == num:
                return False
    return True


def dfs(depth):
    if depth == len(zeros):
        for row in boards:
            print(*row)
        exit()

    nr, nc = zeros[depth]
    for num in range(1, 10):
        if check_row(nr, num) and check_col(nc, num) and check_square(nr, nc, num):
            boards[nr][nc] = num
            dfs(depth + 1)
            boards[nr][nc] = 0


boards = [list(map(int, input().split())) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if boards[i][j] == 0:
            zeros.append((i, j))

dfs(0)
