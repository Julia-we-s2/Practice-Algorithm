data = []
c, n = map(int, input().split())

min_cost = [1e9 for _ in range(c + 100)]
min_cost[0] = 0
for _ in range(n):
    cost, customer = map(int, input().split())
    data.append((cost, customer))

data_sort = sorted(data, key=lambda x: x[0])

for cost, customer in data_sort:
    for i in range(customer, c + 100):
        min_cost[i] = min(min_cost[i - customer] + cost, min_cost[i])

print(min(min_cost[c:]))
