m = int(input())
n = int(input())

li = []
err = False

for i in range(m, n+1):
    if i == 1:
        continue
    
    for j in range(2, i):
        if i % j == 0:
            err = True
            break

    if err is False:
        li.append(i)

    err = False

if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)
