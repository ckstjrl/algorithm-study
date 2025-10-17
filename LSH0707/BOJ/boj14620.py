import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_cost = float('inf')
def pf(i, j):  # (i, j) 좌표에 꽃을 심을 수 있으면 True 안되면 False 반환
    for di, dj in [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni = i + di
        nj = j + dj
        if visited[ni][nj] == 1:
            return False
    return True

def cal_cost(i, j, x):
    # (i, j)좌표에 심었을 때 cost를 반환하고 visited의 값을 x로 바꿈
    cost = 0
    for di, dj in [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni = i + di
        nj = j + dj
        cost = cost + arr[ni][nj]
        visited[ni][nj] = x
    return cost

def flower(cnt, a_cost):  # (심은 꽃 수, 누적 코스트)
    global min_cost
    if a_cost >= min_cost:
        return
    if cnt == 3:
        if min_cost > a_cost:
            min_cost = a_cost
        return
    for i in range(1, N-1):
        for j in range(1, N-1):
            if pf(i, j):  # 꽃을 심을 수 있으면
                cost = cal_cost(i, j, 1)  # cost계산 후, visited = 1
                flower(cnt + 1, a_cost + cost)
                cal_cost(i, j, 0)  # visited = 0 으로 백트래킹

flower(0, 0)
print(min_cost)
