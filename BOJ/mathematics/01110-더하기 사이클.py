n = int(input())
num = n
cycle = 0

while 1:
    a = num // 10
    b = num % 10
    num = b * 10 + (a + b) % 10
    cycle += 1

    if num == n:
        print(cycle)
        break