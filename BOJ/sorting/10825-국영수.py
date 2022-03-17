n = int(input())
li = [list(input().split()) for _ in range(n)]

li.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in li:
    print(i[0])