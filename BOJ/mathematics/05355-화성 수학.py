t = int(input())

for i in range(t):
    equations = list(input().split())
    num = float(equations[0])
    calcs = equations[1:]

    for each in calcs:
        if each == '@':
            num *= 3
        elif each == '%':
            num += 5
        elif each == '#':
            num -= 7

    print('%0.2f' % num)
