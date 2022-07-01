# 2470 번째 문제와의 차이는 오름차순으로 정렬된지 아닌지 밖에 없다.

n = int(input())
li = list(map(int, input().split()))

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

    if total >= 0:
        end -= 1
    else:
        start += 1

print(*res)
