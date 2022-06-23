# list 이용 (시간 3756 ms) vs set 이용 (시간 144 ms)
# set() 이 이렇게나 더 빠른 줄은 처음 알았다

# set 에 원소를 더하게 되면 string 끝에 '\n' 도 붙는다 (그냥 참고 사항)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
strings = set()
cnt = 0

for _ in range(n):
    strings.add(input())

for _ in range(m):
    if input() in strings:
        cnt += 1

print(cnt)
