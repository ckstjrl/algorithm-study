import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
ans = deque()
for i in range(N):  # 리스트 순회하며 조건에 맞는 값 출력
    if arr[i][0] == 'push':
        ans.append(int(arr[i][1]))
    elif arr[i][0] == 'pop':
        if len(ans) > 0:
            print(ans.popleft())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(ans))
    elif arr[i][0] == 'empty':
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'front':
        if len(ans) > 0:
            print(ans[0])
        else:
            print(-1)
    elif arr[i][0] == 'back':
        if len(ans) > 0:
            print(ans[-1])
        else:
            print(-1)