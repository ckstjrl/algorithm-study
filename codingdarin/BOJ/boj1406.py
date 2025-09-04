# 1406 에디터 (D3)
import sys
input = sys.stdin.readline

txt = list(input().strip())
N = int(input())
stack = []  # 커서 이동 시 오른쪽 내용 저장에 쓸 스택

for i in range(N):
    # 각각의 명령어를 독립적으로 수행해주겠다
    act = list(input().split())

    if act[0] == 'L' and txt:
        stack.append(txt.pop())
    elif act[0] == 'D' and stack:
        txt.append(stack.pop())
    elif act[0] == 'B' and txt:
        txt.pop()
    elif act[0] == 'P':
        txt.append(act[1])
while stack:
    txt.append(stack.pop())

print(''.join(txt))
