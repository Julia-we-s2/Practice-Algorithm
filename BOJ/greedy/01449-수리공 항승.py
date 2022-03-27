n, l = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
cnt = 1

start = li[0]
end = li[0] + l - 0.5

for i in li:
    if i <= end:
        continue
    else:
        cnt += 1
        end = i + l - 0.5

print(cnt)
