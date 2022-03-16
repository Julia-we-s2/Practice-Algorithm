li = [int(input()) for _ in range(9)]
total = sum(li)

for i in range(8):
    for j in range(i+1, 9):
        if total - (li[i] + li[j]) == 100:
            num1 = li[i]
            num2 = li[j]

            li.remove(num1)
            li.remove(num2)
            
            li.sort()

            for k in li:
                print(k)
            exit(0)
