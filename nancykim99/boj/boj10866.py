# BOJ10866. 덱

import sys
from collections import deque

N = int(sys.stdin.readline())

d = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    cmd = command[0]

    if cmd == 'push_front':
        d.appendleft(command[1])
    elif cmd == 'push_back':
        d.append(command[1])
    elif cmd == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif cmd == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif cmd == 'size':
        print(len(d))
    elif cmd == 'empty':
        print(1 if not d else 0)
    elif cmd == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    elif cmd == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])