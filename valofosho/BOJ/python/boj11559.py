"""
BOJ11559 - Puyo Puyo
문제 정리
1. 뿌요는 중력의 영향을 받아 다른 뿌요나 바닥을 만날때까지 내려간다.
2. 같은 색 뿌요가 4개이상 상하좌우로 연결되어 있으면 같은 색 뿌요들이 한 번에 없어진다 -> 1연쇄
3. 연쇄 이후에 다시 1~2번을 반복한다.
4. 터질 수 있는 뿌요가 여러 그룹이면 동시에 터지고, 여러 그룹이 터져도 한 번의 연쇄로 처리
5. 입력으로 주어지는 1번이 완료된 상태의 뿌요에서 몇 연쇄가 되는지 출력해라!

로직 정리
1.visited를 하나 선언(선언 시기 중요!)
2. '.' 가 나왔다는 건 그 위에는 아무런 의미가 없다는 증거
3. probe 함수의 시작점은 아래에서 부터 찾자
4. 아래에서 하나씩 찾아보면서 넣어두고 1연쇄가 끝나면 visited 초기화
5. 메인블록에서 하나씩 찾아서 넣어두고 
"""

from collections import deque

def check(i, j):
    if 0<= i <N and 0<= j < M:
        return True
    else:
        return False

def bfs(i,j):
    q = deque([(i,j)])
    line = [(i,j)]
    cnt = 1
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni, nj) and not visited[ni][nj] and maps[i][j] == maps[ni][nj]:
                visited[ni][nj] = True
                q.append((ni,nj))
                line.append((ni,nj))
                cnt += 1
    # 같은 뿌요가 연이어 4개면 연쇄
    return line

N, M = 12, 6
maps = [list(input()) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0 ,-1, 0]

chain = 0
while True:
    visited = [[False] * M for _ in range(N)]
    pop_list = []
    popped = False
    # 아래부터 순회
    for i in range(N-1, -1, -1):
        for j in range(M):
            if not visited[i][j] and maps[i][j] != '.':
                visited[i][j] = True
                # 만약 연쇄라면
                puyos = bfs(i,j)
                if len(puyos) >= 4:
                    pop_list.extend(puyos)
                    popped = True
    if popped:
        for (x, y) in pop_list:
            maps[x][y] = '.'
        for j in range(M):
            temp = []
            # 아래에서 부터 탐색
            for i in range(N-1, -1, -1):
                if maps[i][j] != '.':
                    temp.append(maps[i][j])
            r = N -1
            for v in temp:
                maps[r][j] = v
                # 다음 자리로 이동
                r -= 1
            for i in range(r, -1, -1):
                maps[i][j] = '.'
        chain += 1
    else:
        break
print(chain)

