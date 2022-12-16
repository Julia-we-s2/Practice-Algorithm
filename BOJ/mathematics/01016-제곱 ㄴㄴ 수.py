min_val, max_val = map(int, input().split())

ans = max_val - min_val + 1
check = [False for _ in range(ans)]

for i in range(2, int(max_val ** 0.5 + 1)):
    square_num = i * i
    for j in range((((min_val - 1) // square_num) + 1) * square_num, max_val + 1, square_num):
        if not check[j - min_val]:
            check[j - min_val] = True
            ans -= 1
print(ans)
