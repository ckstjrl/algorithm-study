"""
BOJ18111. 마인크래프트

[문제]
팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다.
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.
목재를 충분히 모은 lvalue는 집을 짓기로 하였다.
하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.
lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.

1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.
밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

[입력]
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다.
(i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

[출력]
첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
"""

import sys
input = sys.stdin.readline

def flatten_terrain(h, B, min_h, max_h, counts):    # 목표 높이 h에 맞춰 땅을 평탄화할 때 걸리는 시간 및 가능 여부을 구하는 함수

    dug_ups = 0 # 파낸 블록의 개수
    fills = 0   # 채울 블록의 개수

    # 높이별 블록 개수를 활용하여 파낼/채울 블록의 개수 계산
    for height in range(min_h, max_h + 1):
        if counts[height] == 0: # 땅이 목표 높이와 같으면 pass
            continue
        if height > h:  # 땅이 목표 높이보다 높으면 블록을 파냄
            dug_ups += (height - h) * counts[height]
        elif height < h:  # 땅이 목표 높이보다 낮으면 블록을 채움
            fills += (h - height) * counts[height]

    # 인벤토리에 있는 블록(= 초기 B + 제거한 블록)보다 채울 블록이 더 많이 필요하면 불가능
    if dug_ups + B < fills:
        return 21e9, False

    # 총 시간 = 제거(2초) + 채우기(1초)
    time = dug_ups * 2 + fills
    return time, True


# main
MIN_HEIGHT = 0
MAX_HEIGHT = 256
N, M, B = map(int, input().split())

# counts[h] = 높이가 h인 칸의 개수
counts = [0] * (MAX_HEIGHT + 1)
min_h, max_h = MAX_HEIGHT, MIN_HEIGHT  # 실제 입력의 최소/최대 높이를 추적할 변수 min_h, max_h를 초기화

# 입력받으며 각 높이의 개수를 세고, 최소/최대 높이 갱신
for _ in range(N):
    row = list(map(int, input().split()))
    for h in row:
        counts[h] += 1
        if h < min_h:
            min_h = h
        if h > max_h:
            max_h = h

# 결과 저장용 변수 : 최소 작업 시간과 평탄화 높이를 초기화
min_time = 21e9
flattened_height = 0

# 가능한 목표 높이(min_h ~ max_h)만 탐색 (0~256 전부 볼 필요 없어서 연산량 감소)
for h in range(min_h, max_h + 1):
    time, possible = flatten_terrain(h, B, min_h, max_h, counts)
    # 최소 시간 갱신 (시간이 같다면 더 높은 높이가 선택됨)
    if possible and time <= min_time:
        min_time = time
        flattened_height = h

# 최소 작업 시간과 그때의 평탄화 높이를 출력
print(min_time, flattened_height)

"""
# 실패 코드(시간 초과) : brute-force 방식

# TLE 이유? 연산량 많아서
# 높이 후보 : 0 ~ 256 -> 257
# 각 높이마다 N * M 전부 확인 -> 최대 500 * 500
# 따라서, 최대 연산량은 257 * 500 * 500 = 64250000 -> TLE
# 결국 "카운트 배열"을 이용해 연산량을 줄여서 해결했다!
# 역시 S2 문제를 그냥 구현하는 건 무리무리... 연산량 생각하면서 하자

def flatten_terrain(h, B):
    time = 0
    inventory = B
    possible = True
    for i in range(N):
        for j in range(M):
            if terrain[i][j] > h:
                dug_ups = terrain[i][j] - h
                time += 2 * dug_ups
                inventory += dug_ups
            elif terrain[i][j] < h:
                fills = h - terrain[i][j]
                time += 1 * fills
                inventory -= fills
                if inventory < 0:
                    possible = False
            else:
                continue
    return time, possible

# main
MIN_HEIGHT = 0
MAX_HEIGHT = 256
N, M, B = map(int, input().split())
terrain = [list(map(int, input().split())) for _ in range(N)]
min_time = 21e9
flattened_height = MIN_HEIGHT
for h in range(MIN_HEIGHT, MAX_HEIGHT + 1):
    time, possible = flatten_terrain(h, B)
    if possible and time <= min_time:
        min_time = time
        flattened_height = h
print(f'{min_time} {flattened_height}')
"""