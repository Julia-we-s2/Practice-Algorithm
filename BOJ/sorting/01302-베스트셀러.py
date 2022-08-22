from collections import defaultdict

dic = defaultdict(int)
n = int(input())

for _ in range(n):
    book = input()
    dic[book] += 1

max_frequency = max(dic.values())
li = []

for book, amount in dic.items():
    if amount == max_frequency:
        li.append(book)

print(sorted(li)[0])
