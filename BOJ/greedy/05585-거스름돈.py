n = int(input())
li = [500, 100, 50, 10, 5, 1]
change = 1000 - n
cnt = 0

for i in li:
    cnt += change // i
    change %= i

print(cnt)