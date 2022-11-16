def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a != parent_b:
        parent[parent_b] = parent_a
        number[parent_a] += number[parent_b]


tc = int(input())

for case in range(tc):
    parent = {}
    number = {}

    f = int(input())
    for _ in range(f):
        a, b = input().split(" ")

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])
