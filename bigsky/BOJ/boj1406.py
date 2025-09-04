# BOJ1406: 에디터
import sys
from collections import deque
input = sys.stdin.readline

ls1 = deque(input().strip())  # 커서의 왼쪽 부분
ls2 = deque()  # 커서의 오른쪽 부분

M = int(input())
for _ in range(M):
    cmd = input().strip().split()
    if len(cmd) == 1:
        if cmd[0] == 'L' and ls1: # 왼쪽에서 오른쪽으로 옮기기
            ls2.appendleft(ls1.pop())
        elif cmd[0] == 'D' and ls2: # 오른족에서 왼쪽으로 옮기기
            ls1.append(ls2.popleft())
        elif cmd[0] == 'B' and ls1: # 왼쪽 지우기
            ls1.pop()
    else: # 왼쪽에 문자 추가
        ls1.append(cmd[1])

ans = ''.join(ls1 + ls2)
print(ans)   