n, m = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

print(*sorted(a_li + b_li))