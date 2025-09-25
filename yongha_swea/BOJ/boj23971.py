import math

#H, N: 총 행, 행 간격
#W, M: 총 열, 열 간격
H, W, N, M = map(int, input().split())

#가능한 행의 수
r = math.ceil(H / (N + 1))

#가능한 열의 수
c = math.ceil(W / (M + 1))

#가로 * 세로 진행
print(r * c)