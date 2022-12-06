while True:
    words = input()
    if words == '#':
        break

    cnt = 0
    for each in words:
        if each.lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print(cnt)
    