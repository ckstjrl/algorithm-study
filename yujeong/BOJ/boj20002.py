# 20002. 사과나무

import sys
input = sys.stdin.readline

N = int(input())
farm = [list(map(int, input().split())) for _ in range(N)]

# 누적합 이차원 리스트
newfarm = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        # (i, j) 까지의 누적합 
        # = [원래 농장에서 그 칸 값] + [행, 열 각각 -1칸씩에서 누적합] - [중복된 영역]
        newfarm[i][j] = farm[i-1][j-1] + newfarm[i-1][j] + newfarm[i][j-1] - newfarm[i-1][j-1]

max_v = -1000

# 부분합 구하기
for k in range(N): 
    for x in range(1, N-k+1):
        for y in range(1, N-k+1):
            # (x, y)에서부터 가로세로 k칸 부분합 
            # = [(x+k, y+k)까지 누적합] - [행, 열 각각 정사각형에서 빠지는 부분 누적합] + [중복된 영역]
            temp_sum = newfarm[x+k][y+k] - newfarm[x-1][y+k] - newfarm[x+k][y-1] + newfarm[x-1][y-1]
            max_v = max(max_v, temp_sum)

print(max_v)