'''
BOJ20002 : 사과나무 (G5)

해결 방법 : 
2차원 누적합을 구하기 -> 그 후 브루트포스 돌리기

메모 : 
2차원 누적합 구하는 법
```
psum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = (board[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1])

def get_sum(x1, y1, x2, y2):
    return (psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1])
```

음수까지 있을 때, 최댓값 갱신하기 위한 값
`answer = -10**18`
'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

psum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = (board[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1])

def get_sum(x1, y1, x2, y2):
    return (psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1])

answer = -10**18
for size in range(1, N + 1):
    for i in range(1, N - size + 2):
        for j in range(1, N - size + 2):
            x2, y2 = i + size - 1, j + size - 1
            total = get_sum(i, j, x2, y2)
            answer = max(answer, total)

print(answer)
