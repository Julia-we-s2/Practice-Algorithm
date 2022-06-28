# deque 를 사용해야 시간 초과가 안 난다

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    command = input().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if not queue else 0)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)
