def check_password(cnt, idx):
    if cnt == l:
        vowel, consonant = 0, 0

        for i in range(l):
            if ans[i] in vowels:
                vowel += 1
            else:
                consonant += 1

        if vowel >= 1 and consonant >= 2:
            print(''.join(ans))

        return

    for i in range(idx, c):
        ans.append(alphabets[i])
        check_password(cnt + 1, i + 1)
        ans.pop()


vowels = {'a', 'e', 'i', 'o', 'u'}
l, c = map(int, input().split())
alphabets = sorted(list(input().split()))
ans = []

check_password(0, 0)

