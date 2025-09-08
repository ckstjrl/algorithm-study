from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):  # 명령어 입력받아서 조건에 맞게 덱에 추가, 제거 및 값 출력
    a = list(map(str, input().split()))
    if a[0] == 'push_front':  
        q.appendleft(a[1])
    elif a[0] == 'push_back':
        q.append(a[1])
    elif a[0] == 'pop_front':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
