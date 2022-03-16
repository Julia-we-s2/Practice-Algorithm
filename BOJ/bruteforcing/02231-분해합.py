n = int(input())

for i in range(1, n+1):
    total = i
    total += sum(list(map(int, str(i))))

    if total == n:
        print(i)
        break
    if i == n:
        print(0)