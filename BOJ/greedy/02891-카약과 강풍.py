n, s, r = map(int, input().split())

demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

li = [1] * n

for i in demaged:
    li[i-1] -= 1

for j in extra:
    li[j-1] += 1

for k in range(len(li)):
    if li[k] == 0:
        if k == 0:
            if li[k+1] == 2:
                li[k+1] = 1
                li[k] = 1
    
        elif k == len(li)-1:
            if li[k-1] == 2:
                li[k-1] = 1
                li[k] = 1
    
        else:
            if li[k-1] == 2:
                li[k-1] = 1
                li[k] = 1
                continue              
            if li[k+1] == 2:
                li[k+1] = 1
                li[k] = 1
                continue
    else:
        continue

print(li.count(0))
