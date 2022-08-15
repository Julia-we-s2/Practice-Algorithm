n = int(input())
list_len = 0
ans = []

for i in range(0, n + 1):
    temp = [n, i]
    first = n
    j = 0
    while True:
        second = temp[j] - temp[j + 1]
        if second < 0:
            break
        temp.append(second)
        j += 1

        if len(temp) > list_len:
            list_len = len(temp)
            ans = temp[:]

print(list_len)
print(*ans)
