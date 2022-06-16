def binary_search(target):
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if note_1[mid] == target:
            return 1
        elif note_1[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


t = int(input())

for tc in range(t):
    n = int(input())
    note_1 = sorted(list(map(int, input().split())))
    m = int(input())
    note_2 = list(map(int, input().split()))

    for i in range(m):
        print(binary_search(note_2[i]))

