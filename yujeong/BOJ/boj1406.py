# 1406. 에디터

import sys
input = sys.stdin.readline
from collections import deque

left = deque(input().strip())       # 커서 왼쪽에 있는 문자열 (인덱스 작을수록 커서에서 멂)
right = deque()                     # 커서 오른쪽에 있는 문자열 (인덱스 작을수록 커서에서 가까움)

M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':               # 명령어가 'L'이면
        if left:                    # (커서를 왼쪽으로 옮길 수 있으면) 왼쪽으로 한칸
            right.append(left.pop())    # 즉, 문자 1개가 왼쪽에서 오른쪽으로 이동

    elif cmd[0] == 'D':             # 명령어가 'R'이면
        if right:                   # 마찬가지로 오른쪽으로 한칸
            left.append(right.pop())

    elif cmd[0] == 'B':             # 명령어가 'B'이면
        if left:                    # (커서 왼쪽에 문자가 있으면) 문자 1개 삭제
            left.pop()

    elif cmd[0] == 'P':             # 명령어가 'P'이면
        left.append(cmd[1])         # 문자를 커서 왼쪽에 추가

# 출력: 커서 왼쪽은 인덱스 순서대로, 오른쪽은 인덱스 역순으로 join
print(''.join(left) + ''.join(reversed(right)))