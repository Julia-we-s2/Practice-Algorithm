import sys

input = sys.stdin.readline
n, k, b = map(int, input().split())
arr = [0] * (n + 1)

for _ in range(b):
    arr[int(input())] = 1

window_sum = sum(arr[1: k + 1])
min_break = window_sum

for i in range(2, n - k + 2):
    window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
    min_break = min(window_sum, min_break)
    if min_break == 0:
        break

print(min_break)
