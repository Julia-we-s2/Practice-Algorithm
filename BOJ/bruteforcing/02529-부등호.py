def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j
    return 1


def solve(depth, li):
    global maximum, minimum

    if depth == k + 1:
        if len(minimum) == 0:
            minimum = li
        else:
            maximum = li
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or possible(li[-1], str(i), signs[depth - 1]):
                visited[i] = 1
                solve(depth + 1, li + str(i))
                visited[i] = 0


k = int(input())
signs = list((input().split()))

visited = [0] * 10
maximum, minimum = '', ''

solve(0, '')
print(maximum)
print(minimum)