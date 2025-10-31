# BOJ 2638. 치즈 / D3
'''
문제
N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다.
단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다.
이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다.
그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다.
따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.

<그림 1>

<그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다.
그러므로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다.
그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.

<그림 2>

<그림 3>
모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다.
입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다.
그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다.
또한, 각 0과 1은 하나의 공백으로 분리되어 있다.

출력
출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

outside = [[0]*M for _ in range(N)] # 외부 공기 확인

def inside(arr): # 외부 공기 내부 공기 판단, 외부공기는 1로 내부 공기는 0으로 리턴
    visited = [[0]*M for _ in range(N)]
    q = deque()

    # 테두리 중 값이 0인 칸들을 시작점으로
    for r in range(N):
        for c in (0, M-1):
            if arr[r][c] == 0 and not visited[r][c]:
                visited[r][c] = 1
                q.append((r, c))
    for c in range(M):
        for r in (0, N-1):
            if arr[r][c] == 0 and not visited[r][c]:
                visited[r][c] = 1
                q.append((r, c))

    # BFS: 0만 따라가며 확장
    while q:
        r, c = q.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

    return visited  # 외부 공기면 1, 내부(막힌) 0이면 0


def cheese(arr): # 치즈가 있는 좌표 추출하는 함수
    c_axis = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                c_axis.append((i, j))
    return c_axis


def m_or_s(i, j): # 해당 좌표가 녹는지 아닌지 확인하는 함수
    cnt = 0
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and outside[ni][nj] == 1: # 외부공기 두개 이상일 때 녹는다
            cnt += 1
    if cnt >= 2:
        return 1
    else: return 0


clear = [[0]*M for _ in range(N)]
time = 0
while arr != clear: # while문 정지 조건으로 clear 리스트 만들고 이와 arr가 동일 해지는 경우 루프 탈출
    outside = inside(arr) # 계속 외부 공기 내부 공기 확인

    cheese_axis = cheese(arr) # 치즈 좌표 저장

    melt = [] # 녹는 좌표 리스트
    for a in cheese_axis:
        y, x = a
        m_s = m_or_s(y, x) # 녹는지 안 녹는지 판단
        if m_s == 1:
            melt.append(a) # 녹으면 녹는 좌표 리스트에 넣음

    for b in melt: # 리스트에 넣은 좌표들 한번에 제거
        s, t = b
        arr[s][t] = 0

    time += 1 # 루프 한번당 time +1


print(time)

'''
1. 외부 공기 내부 공기를 먼저 판단하는 함수 제작
2. 치즈가 있는 좌표 찾는 함수 제작
3. 치즈가 녹는지 안 녹는지 판단하는 함수 제작
4. while문을 통해서 녹는지 안녹는지 판단하고 한번에 녹는 치즈 제거한 후 완전 다 빌때까지 루프 돌리기
'''
