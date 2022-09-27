while True:
    n = int(input())
    if n == -1:
        break
    temp = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            temp.append(i)
    if sum(temp) != n:
        print(n, 'is NOT perfect.')
    else:
        s = ' + '.join(map(str, temp))
        print(n, '=', s)
