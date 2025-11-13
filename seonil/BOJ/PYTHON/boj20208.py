"""
BOJ20208. 진우의 민트초코우유

[문제]
진우는 민트초코우유를 좋아하는 민초단이다. 힘든 일이 있더라도 민트초코우유 하나를 마시면 기운이 펄펄 솟는다고 한다!
민트초코우유를 너무 좋아하는 나머지 진우는 매일 아침 특정 지역들에서 민트초코우유가 배달된다는 N × N 크기의 2차원 민초마을로 이사를 하였다.
진우는 아침에 눈을 뜨면 집에서 민초마을의 지도를 들고 민트초코우유를 찾으러 출발한다.
이때의 초기 체력은 M이다. 여기에서 체력은 진우가 이동할 수 있는 거리를 나타낸다.
진우는 지도상에서 상, 하, 좌, 우로 1칸씩 이동할 수 있으며 이동하면 체력이 1만큼 줄어든다. 진우가 마을을 돌아다니다가 민트초코우유를 마신다면 체력이 H 만큼 증가하며 진우의 체력이 초기체력 이상으로 올라갈 수 있다. 체력이 0이 되는 순간 진우는 이동할 수 없다.
민트초코를 찾으러 돌아다니다가 마을 한복판에서 체력이 0이 되어 집으로 못 돌아가는 상황은 만들어져서는 안된다.
진우가 얼마나 많은 민트초코우유를 마시고 집으로 돌아올 수 있는지 알아보자.

[입력]
첫번째 줄에 민초마을의 크기인 N과 진우의 초기체력 M, 그리고 민트초코우유를 마실때 마다 증가하는 체력의 양 H가 공백을 두고 주어진다. N, M, H는 모두 10보다 작거나 같은 자연수이다.
두번째 줄부터 N+1번째 줄에 N칸에 걸쳐서 민초마을의 지도가 주어진다. 각 칸은 공백을 두고 주어지며 지도상에서 진우의 집은 1, 민트초코우유는 2로 주어지며 빈 땅은 0으로 주어진다.
진우의 집은 무조건 한 곳이 주어지며 마을에 배달되는 민트초코우유의 총합은 10개를 넘지 않는다.

[출력]
진우가 집을 나와서 다시 집으로 돌아올 때 까지 마실 수 있는 민트초코우유의 최대 개수를 출력하자.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# 현재 위치 (y, x)에서 시작해 남은 체력으로 마실 수 있는 모든 민트초코우유 조합을 DFS + 백트래킹으로 탐색하는 함수
def find_max_mintchoco_milks(y, x, cur_hp, heal, cnt):

    global max_mcms
    global hy, hx

    # 현재 위치에서 집까지 거리 계산
    home_dist = abs(y - hy) + abs(x - hx)

    # 만약 남은 체력으로 집에 돌아갈 수 있다면, 민최몇 기록 갱신
    if cur_hp >= home_dist:
        max_mcms = max(cnt, max_mcms)
    
    # 모든 민트초코우유 좌표를 확인
    for idx, each in enumerate(mcm_locs):
        if visited_mcm[idx]:
            continue    # 이미 방문해서 마셨던 민트초코우유는 skip
        ey, ex = each
        dist = abs(y - ey) + abs(x - ex)  # 현재 위치부터 각각의 방문하지 않은 민트초코우유까지의 거리 dist를 계산
        
        # 방문하지 않은 민트초코우유까지 현재 체력으로 이동 가능하다면
        if cur_hp >= dist:
            visited_mcm[idx] = True  # 그 민트초코우유로 이동하여 마신다
            find_max_mintchoco_milks(ey, ex, cur_hp - dist + heal, heal, cnt + 1)   # 해당 민트초코우유 좌표로 이동, (현재 체력 - 이동 거리 + 회복량)으로 체력 갱신, 마신 민트초코우유 count
            visited_mcm[idx] = False  # 백트래킹

# main
N, M, H = map(int, input().split()) # N: 마을 크기, M: 초기 체력, H: 민트초코우유 회복량 입력
village = [list(map(int, input().split())) for _ in range(N)]   # 마을 정보 입력

mcm_locs = []   # 민트초코우유 위치 리스트

# 모든 마을 좌표를 순회하면서,
for y in range(N):
    for x in range(N):
        if village[y][x] == 1:  # 진우의 집이면,
            hy, hx = y, x       # 진우의 집 위치 저장
        elif village[y][x] == 2:    # 민트초코우유라면,
            mcm_locs.append((y, x)) # 민트초코우유의 좌표를 mcm_locs에 넣기

# 각 민트초코우유의 방문 여부 체크
visited_mcm = [False] * len(mcm_locs)

# 민최몇 기록(집을 나와서 다시 집으로 돌아올 때까지 마실 수 있는 민트초코우유의 최대 개수)
max_mcms = 0

# DFS 탐색 시작
find_max_mintchoco_milks(hy, hx, M, H, 0)

# 진우의 민최몇 기록 출력
print(max_mcms)
