# 1018. 체스판 다시 칠하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
paint = []

# 맨 왼쪽 위 칸이 흰색인 경우
w_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# 검은색인 경우 
b_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

for i in range(N-7):
    for j in range(M-7):
        # 8x8 크기 영역에서
        subarr = [a[j:j+8] for a in arr[i:i+8]]
        paint_w = 0
        paint_b = 0
        for x in range(8):
            for y in range(8):
                # 색을 칠하는 경우의 수 1 
                if subarr[x][y] != w_board[x][y]:
                    paint_w += 1
                
                # 색을 칠하는 경우의 수 2
                if subarr[x][y] != b_board[x][y]:
                    paint_b += 1

        # 둘 중 더 적게 칠하는 수를 기록 
        paint.append(min(paint_b, paint_w))
        
# 색을 칠하는 사각형 개수가 최소가 되는 경우를 출력 
print(min(paint))