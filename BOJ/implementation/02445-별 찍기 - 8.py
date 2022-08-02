# 여백이 2, 4, 6, .. 일거라고는 생각을 못 했었지 

n = int(input())

for i in range(1, n):
    print('*' * i + ' ' * 2 * (n - i) + '*' * i)

for j in range(n, 0, -1):
    print('*' * j + ' ' * 2 * (n - j) + '*' * j)
