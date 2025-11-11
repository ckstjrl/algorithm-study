# BOJ 6087. 레이저 통신 / D3
'''
크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.

'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.

레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.

아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.

7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
입력
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)

둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.

.: 빈 칸
*: 벽
C: 레이저로 연결해야 하는 칸
'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.

출력
첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
area = [list(input().strip()) for _ in range(H)]

def find_c(arr):
    c_axis = []
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'C':
               c_axis.append((i, j))
    return c_axis

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 하 상 우 좌

INF = 1e9
visited = [[[INF]*4 for _ in range(W)] for _ in range(H)] # i, j, dir까지 체크해야해서 3차원 배열
q = deque()

laser = find_c(area)
si, sj = laser[0]
ei, ej = laser[1]

for d in range(4):
    q.append((si, sj, d))
    visited[si][sj][d] = 1


while q:
    i, j, dir = q.popleft()

    for nd, (di, dj) in enumerate(dirs):
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and area[ni][nj] != '*':
            mirror = visited[i][j][dir]
            if nd != dir:
                mirror += 1

            if visited[ni][nj][nd] > mirror:
                visited[ni][nj][nd] = mirror
                q.append((ni, nj, nd))

ans = min(visited[ei][ej])
print(ans-1) # 시작할때 값 빼주기

'''
BFS + 다익스트라
visited를 3차원 배열로 제작하고
큐에 좌표와 어디방향에서 왔는지를 저장하므로 한번에 확인 가능
처음 시작할 때 상하좌우 다 이동하는 걸 넣고 시작함.
mirror = visited[i][j][dir]로 설정하고
BFS와 같이 진행하면서 방향이 바뀔때마다 1식 추가해주는 과정을 거침
그리고 visited[ni][nj[nd]가 mirror보다 크다면 mirror값으로 최신화
그 지점까지 오는데 방향을 가장 적게 바꾼 값으로 변경하는 과정
그러면 각 방향에서 시작해서 도착점까지 방향을 바꾸는 횟수들이 visited[ei][ej]에 list로 저장
답은 여기서 최솟값 추출
'''