# 10845. 큐
import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    cmd = input().split()

    # 명령 'push'
    if cmd[0] == 'push':
        q.append(int(cmd[1]))   # 다음으로 주어진 정수를 큐에 넣기
    
    # 명령 'pop'
    elif cmd[0] == 'pop':
        if q:                   # 큐가 비어있지 않으면
            print(q.popleft())  # 가장 앞 정수 빼고 출력
        else:                   # 비어있으면
            print(-1)           # -1 출력
    
    # 명령 'size'
    elif cmd[0] == 'size':
        print(len(q))           # 큐에 들어있는 원소 개수 출력
    
    # 명령 'empty'
    elif cmd[0] == 'empty':
        if q:                   # 큐가 비어있지 않으면
            print(0)            # 0 출력
        else:                   # 비어있으면
            print(1)            # 1 출력

    # 명령 'front'
    elif cmd[0] == 'front':
        if q:                   # 큐가 비어있지 않으면
            print(q[0])         # 가장 앞 정수 출력
        else:                   # 비어있으면
            print(-1)           # -1 출력
    
    # 명령 'back'
    else:
        if q:                   # 큐가 비어있지 않으면
            print(q[-1])        # 가장 뒤 정수 출력
        else:                   # 비어있으면
            print(-1)           # -1 출력