n = int(input())
li = sorted(list(map(int, input().split())))

start = 0
end = n - 1
ans = abs(li[start] + li[end])
res = [li[start], li[end]]

while start < end:
    total = li[start] + li[end]

    if abs(total) < ans:
        ans = abs(total)
        res = [li[start], li[end]]
        if ans == 0:
            break

    if total < 0:
        start += 1
    else:
        end -= 1

print(*res)

