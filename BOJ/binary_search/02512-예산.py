n = int(input())
li = sorted(list(map(int, input().split())))
m = int(input())

start, end = 0,  max(li)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for num in li:
        if num >= mid:
            total += mid
        else:
            total += num

    if total > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)
