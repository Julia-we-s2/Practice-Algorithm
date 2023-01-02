n, m = map(int, input().split())
used_memories = [0] + list(map(int, input().split()))
unactivate_costs = [0] + list(map(int, input().split()))

knapsack = [[0 for _ in range(sum(unactivate_costs) + 1)] for _ in range(n + 1)]
res = sum(unactivate_costs)

for i in range(1, n + 1):
    byte = used_memories[i]
    cost = unactivate_costs[i]

    for j in range(1, sum(unactivate_costs) + 1):
        if j < cost:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - cost] + byte, knapsack[i - 1][j])

        if knapsack[i][j] >= m:
            res = min(res, j)

if m != 0:
    print(res)
else:
    print(0)
    