n, k = map(int, input().split())
arr = list(map(int, input().split()))


window_sum = sum([arr[i] for i in range(k)])
max_sum = window_sum

for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(window_sum, max_sum)

print(max_sum)