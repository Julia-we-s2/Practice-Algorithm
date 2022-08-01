from collections import defaultdict
alphabets = defaultdict(int)

word = input()
for i in word:
    alphabets[i] += 1

for i in 'abcdefghijklmnopqrstuvwxyz':
    if alphabets[i]:
        print(alphabets[i], end=' ')
    else:
        print(0, end=' ')
