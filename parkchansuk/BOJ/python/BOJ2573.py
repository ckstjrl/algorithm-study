# BOJ 2573. 빙산 / D3
'''
지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자.
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다.
빙산 이외의 바다에 해당되는 칸에는 0이 저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.
빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에,
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

def count_ice(sea): # 빙산 덩어리 개수 함수
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if sea[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    ti, tj = q.popleft()
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = ti + di, tj + dj
                        if 0 <= ni < N and 0 <= nj < M and sea[ni][nj] != 0 and visited[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
    return cnt # 빙산 덩어리 개수

def melting(arr): # 빙산 녹는 함수
    melt = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt = 0
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        cnt += 1
                melt[i][j] = cnt
    new_arr = [[0]*M for _ in range(N)] # 빙산의 크기가 음수가 되는 것을 방지하기 위해서 사용
    for a in range(N):
        for b in range(M):
            new_arr[a][b] = max(0, arr[a][b] - melt[a][b])

    return new_arr

ans = 0 # 분리될 때까지 걸린 년수
while True:
    comp = count_ice(sea)
    if comp == 0:        # 분리되기전에 다 녹음
        print(0)
        break
    if comp >= 2:        # 분리되면 바로 출력
        print(ans)
        break
    sea = melting(sea)
    ans += 1

'''
1. 0이 아닌 칸 동서남북으로 0이 몇개 있는지 확인하고 한 사이클 마다 0의 개수만큼 감소시켜야 한다.
2. 매 사이클마다 0이 아닌 숫자들이 몇 덩어리 인지 확인하고 2가 되는 순간 사이클의 횟수를 출력해야한다.
이 방식을 생각하면서 녹는 함수, 빙산 분리 확인 함수를 통하여 진행
빙산 분리 확인 함수의 경우 BFS 사용
녹는 함수의 경우 델타 활용
'''