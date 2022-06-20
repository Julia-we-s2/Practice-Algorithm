t = int(input())

for tc in range(t):
    r, s = input().split()
    p = ''
    for i in s:
        p += int(r) * i
    print(p)