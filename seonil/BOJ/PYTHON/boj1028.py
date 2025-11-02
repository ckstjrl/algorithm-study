"""
BOJ1028. 다이아몬드 광산

[문제]
다이아몬드 광산은 0과 1로 이루어진 R행*C열 크기의 배열이다.
다이아몬드는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 모양이다. 크기가 1, 2, 3인 다이아몬드 모양은 다음과 같이 생겼다.

size 1:    size 2:    size 3:
                         1
              1         1 1
   1         1 1       1   1
              1         1 1
                         1

다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 R과 C가 주어진다. R과 C는 750보다 작거나 같은 자연수이다.
둘째 줄부터 R개의 줄에는 다이아몬드 광산의 모양이 주어진다.

[출력]
첫째 줄에 다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력한다. 만약 다이아몬드가 없을 때는 0을 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# main
R, C = map(int, input().split())
mine = [list(input().strip()) for _ in range(R)]

# DP 배열 초기화
# 각 DP는 해당 방향으로 연속된 '1'의 개수를 저장한다.
# 예) LU[y][x] = (y,x)에서 ↖ 방향으로 연속된 1의 개수
LU = [[0] * C for _ in range(R)]  # ↖ 방향
RU = [[0] * C for _ in range(R)]  # ↗ 방향
LD = [[0] * C for _ in range(R)]  # ↙ 방향
RD = [[0] * C for _ in range(R)]  # ↘ 방향

# 위쪽 방향 DP 계산 (↖, ↗)
# 점화식 : mine[y][x] == '1' 이면:
#   LU[y][x] = LU[y-1][x-1] + 1  (↖로 연속)
#   RU[y][x] = RU[y-1][x+1] + 1  (↗로 연속)
for y in range(R):  # 위에서 아래로 내려가며 계산
    for x in range(C):
        if mine[y][x] == '1':
            LU[y][x] = 1
            RU[y][x] = 1
            # 범위 내에서 이전 칸의 정보를 이용
            if y > 0 and x > 0:
                LU[y][x] += LU[y-1][x-1]
            if y > 0 and x < C-1:
                RU[y][x] += RU[y-1][x+1]

# 아래쪽 방향 DP 계산 (↙, ↘)
# mine[y][x] == '1' 이면:
#   LD[y][x] = LD[y+1][x-1] + 1  (↙로 연속)
#   RD[y][x] = RD[y+1][x+1] + 1  (↘로 연속)
for y in range(R-1, -1, -1):  # 아래에서 위로 올라가며 계산
    for x in range(C):
        if mine[y][x] == '1':
            LD[y][x] = 1
            RD[y][x] = 1
            # 범위 내에서 이전 칸의 정보를 이용
            if y < R-1 and x > 0:
                LD[y][x] += LD[y+1][x-1]
            if y < R-1 and x < C-1:
                RD[y][x] += RD[y+1][x+1]

# 각 칸을 "다이아몬드의 꼭짓점(맨 위)"으로 두고 가능한 최대 크기 탐색
# 다이아몬드의 정의:
#   - 위쪽 삼각형과 아래쪽 삼각형이 대칭이어야 함
#   - 위쪽 끝점에서 시작하여 아래로 size-1만큼 내려갔을 때,
#     그 아래쪽 대각선이 충분히 이어져 있어야 함

max_size = 0

for y in range(R):
    for x in range(C):
        if mine[y][x] == '1':
            # (y, x)를 다이아몬드의 꼭짓점으로 볼 때
            # 아래쪽으로 뻗을 수 있는 최대 높이는 ↙, ↘ 방향 중 더 짧은 쪽에 의해 제한됨
            max_possible = min(LD[y][x], RD[y][x])
            
            # 큰 size부터 작은 size 순으로 검사 (효율적)
            for size in range(max_possible, 0, -1):
                bottom_y = y + 2 * (size - 1)  # 다이아몬드의 맨 아래 꼭짓점 좌표
                if bottom_y >= R:
                    continue  # 범위를 벗어나면 불가능
                
                # 다이아몬드의 아래쪽 꼭짓점에서도 ↖, ↗ 방향으로 size개 이상 이어져야 완성
                if LU[bottom_y][x] >= size and RU[bottom_y][x] >= size:
                    max_size = max(max_size, size)
                    break  # 더 큰 size는 이미 확인했으므로 바로 중단

print(max_size) # 결과 출력: 다이아몬드가 전혀 없으면 0, 아니면 최대 크기 출력

"""
# Fail code: TLE(시간 초과)
# 혹시나 시도해봤지만 Brute-Force 기반 구현이라 에러... 열심히 생각해봤지만 더 연산량을 줄일 방법은 DP 말고는 없었다.

def has_diamond(center, size):
    cy, cx = center
    for y in range(cy - size + 1, cy + size):
        for x in range(cx - size + 1, cx + size):
            # 다이아몬드 경계 조건
            if abs(x - cx) + abs(y - cy) == size - 1:
                if mine[y][x] != '1':   # 경계인데 '1'이 아니면 실패
                    return False
            # 경계가 아닌 부분은 무시
    return True

def find_largest_diamond(R, C):
    max_size = (min(R, C) + 1) // 2
    for size in range(max_size, 0, -1):
        for y in range(size - 1, R - size + 1):
            for x in range(size - 1, C - size + 1):
                if has_diamond((y, x), size):
                    return size
    return 0

# main
R, C = map(int, input().split())
mine = [list(input().strip()) for _ in range(R)]
max_diamond_size = find_largest_diamond(R, C)
print(max_diamond_size)
"""