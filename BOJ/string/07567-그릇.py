brackets = list(input())
temp = ''
cnt = 10

for bracket in brackets:
    if temp:
        if temp == bracket:
            cnt += 5
        else:
            cnt += 10
    temp = bracket

print(cnt)
