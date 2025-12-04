# BOJ 4963. 섬의 개수 / D2
'''
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline
def find_land(arr, w, h):
    land_list = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                land_list.append((i, j))
    return land_list

def island(arr, w, h):
    land = find_land(arr, w, h)
    q = deque(land)
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    while q:
        a, b = q.popleft()
        if visited[a][b] != 1:
            q_in = deque([(a, b)])
            visited[a][b] = 1
            cnt += 1
            while q_in:
                i, j = q_in.popleft()
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0],[1, 1], [-1, -1], [1, -1], [-1, 1]]:
                    ni, nj = i + di, j + dj
                    if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        q_in.append((ni, nj))
                        visited[ni][nj] = 1
    return cnt

while True:
    W, H = map(int, input().split())
    if W != 0 and H != 0:
        w, h = W, H
        wleh = [list(map(int, input().split())) for _ in range(h)]
        island_cnt = island(wleh, w, h)
        print(island_cnt)

    else:
        break


'''
입력 처리가 까다로웠음.
testcase의 개수가 따로 제시되지 않고 0 0이 입력되면 종료되는 부분 처리 방식 고민
일단 모든 입력을 while Ture로 계속 반복시키고
0 0이 입력되는 순간 break로 빠져나올 수 있게 작성

섬의 개수의 경우 BFS 활용
먼저 find_land 함수를 통하여 1인 좌표를 모두 리스트에 담음
island 함수를 통해
1의 좌표를 q(큐)에 집어 넣고
while q를 통해 반복하며 하나씩 뽑아서 방문하지 않은 land의 경우 q_in에 넣어줌
다시 while q_in 반복을 통해 상하좌우 대각 총 8가지 방향에서 있는 1을 방문표시하며 섬 하나를 다 체크
이후 while q_in문이 종료되서 다시 while q문이 반복될때 cnt += 1을 통하여 섬의 개수를 세어줌
'''