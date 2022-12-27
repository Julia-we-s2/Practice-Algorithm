import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    arr = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((b, a))
    arr = sorted(arr, key=lambda x: (x[0], -x[1]))

    ans = sys.maxsize
    weight, same = 0, 0
    flag = False

    for i in range(n):
        weight += arr[i][1]
        if i >= 1 and arr[i][0] == arr[i - 1][0]:
            same += arr[i][0]
        else:
            same = 0
        if weight >= m:
            ans = min(ans, arr[i][0] + same)
            flag = True
    print(ans if flag else -1)
