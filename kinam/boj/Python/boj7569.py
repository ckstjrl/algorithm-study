'''boj7569 토마토
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 
상자들을 수직으로 쌓아 올려서 창고에 보관한다.


창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
#최소 일 수 =>> bfs

from collections import deque

M, N, H = map(int, input().split()) #M 가로 N 세로 H 높이
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]


#3차원 델타 선언
#tomatos[k][i][j] 를 생각해보자
#zip(dk, di, dj)로 묶을 것
di = [0, 1, 0, 0, -1, 0]
dj = [1, 0, 0, -1, 0, 0]
dk = [0, 0, 1, 0, 0, -1]

q = deque([])

#시작점 찾기
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[k][i][j] == 1:   #익은토마토 = 시작점
                q.append([k, i, j]) #큐에 넣고 방문표시
                visited[k][i][j] = 1

#[k, i, j]
date = -1   #날짜

# 2차원 이상 리스트에서 0이 있는지 없는지 확인
def has_0(arr):
    return any(any(0 in x for x in y) for y in arr)

#모든 익지 않은 토마토 0이 없어질때까지
while q:
    ck, ci, cj = q.popleft()

    if not has_0(tomatos):
        date = visited[ck][ci][cj] - 1  #맨 처음 visited = 1부터 시작했으므로 -1해줌
        
    for nk, ni, nj in zip(dk, di, dj):
        #다음 인덱스
        fk, fi, fj = ck + nk, ci + ni, cj + nj
        #범위 조건 and 안익은 토마토 and 방문 x
        if 0 <= fk < H and 0 <= fi < N and 0 <= fj < M and tomatos[fk][fi][fj] == 0 and not visited[fk][fi][fj]:
            visited[fk][fi][fj] = visited[ck][ci][cj] + 1   #방문 표시
            q.append([fk, fi, fj])
            tomatos[fk][fi][fj] = 1 #익은 표시

# print(tomatos)
print(date)
