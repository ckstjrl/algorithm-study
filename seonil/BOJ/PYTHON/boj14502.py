"""
BOJ14502. 연구소

[문제]
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

[출력]
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
"""

from collections import deque
import copy

import sys
input = lambda: sys.stdin.readline().rstrip()

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 바이러스를 퍼뜨리는 함수
def bfs(temp):

    # BFS 준비
    queue = deque(viruses)  # 초기 바이러스 위치 리스트부터 시작

    # BFS
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 좌표 꺼내기
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]   # 다음 좌표는 현재 좌표로부터 인접 상하좌우 칸의 좌표로 설정
            if 0 <= nx < N and 0 <= ny < M: # 다음 좌표가 범위 내부이고
                if temp[nx][ny] == 0:   # 빈 칸이면,
                    temp[nx][ny] = 2    # 바이러스 퍼뜨림
                    queue.append((nx, ny))  # 큐에 추가

    # 안전 영역 계산
    safe = sum(row.count(0) for row in temp)
    # 안전 영역의 크기 반환
    return safe

# 벽 k개 선택하는 조합 함수
def combination(i, start, n, k):
    global answer

    # 벽 k개 선택 완료 시
    if i == k:

        # 지도 복사: 원본을 훼손하지 않기 위해 deepcopy
        temp = copy.deepcopy(lab)

        # 선택 3개 위치에 벽 세우기
        for x, y in path:
            temp[x][y] = 1
        
        # BFS로 바이러스 퍼뜨리고 안전 영역 계산
        safe_zone = bfs(temp)

        # 최댓값 갱신
        answer = max(answer, safe_zone)
        return

    # start부터 n-1까지 빈 칸을 순회하며 벽 선택
    for j in range(start, n):
        path.append(empties[j])
        combination(i + 1, j + 1, n, k)
        path.pop()

# main
N, M = map(int, input().split())    # 지도의 세로 크기 N, 가로 크기 M
lab = [list(map(int, input().split())) for _ in range(N)]   # 연구소 지도 정보

answer = 0  # 안전 영역 최대값
path = []   # 현재 선택한 벽 3개의 위치

# 빈 칸, 바이러스 위치 저장
empties = []
viruses = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empties.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))

# 벽 3개를 선택하는 모든 조합 시도
combination(0, 0, len(empties), 3)

# 안전 영역 최대값 출력
print(answer)
