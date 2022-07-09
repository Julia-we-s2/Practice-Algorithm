# for 문을 돌려서 2~ (해당 숫자 -1) 까지 나눴을 때 나머지가 있는지
# 구하고자 했더니 시간 초과가 났다

# 2 부터 해당 숫자의 제곱근까지만 검사하며 소수인지 판별할 수 있다

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
