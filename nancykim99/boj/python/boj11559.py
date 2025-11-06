'''
BOJ11559 / D3): Puyo Puyo

해결 방법 : BFS. 
1. 모든 타일을 탐색해서, 같은 타일 4개 이상이면 없애기.
2. 없애고 나서, 타일들을 다시 내리기.
3. 타일들을 다 내리고 다시 같은 타일 4개 이상이면, 없애기.
4. 더이상 없앨 타일이 없다면, 몇 번 없앴는지 출력하기.

메모 : 타일을 밑으로 내리는 방법이 생각 안 나서 정말 오래걸렸음...
1. 타일 밑으로 내리는 법 : 각 열을 순회하는게 포인트!
    a. 각 열을 거꾸로 올라가면서 .이 아니면 추가하기 : 아래에서 위로 확인하면 순서가 유지됨
    b. 다 '.'으로 바꿔놓기
    c. 각 열을 다시 아래에서부터 채우기 : 밑에서부터 추가되기에, 떨어지는게 됨
'''
from collections import deque

def bfs(i, j):
    global visited
    color = field[i][j]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    vanished_tile = [(i, j)]
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<12 and 0<=nj<6 and field[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                vanished_tile.append((ni, nj))
    
    return vanished_tile

def down(field):
    for j in range(6):
        puyo_queue = deque()
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                puyo_queue.append(field[i][j])
        for i in range(12):
            field[i][j] = '.'
        idx = 0
        while puyo_queue:
            puyo = puyo_queue.popleft()
            field[11 - idx][j] = puyo
            idx += 1

field = [list(input()) for _ in range(12)]
puyopuyo = 0

while True:
    puyo_pop = False
    visited = [[0]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                vanished = bfs(i, j)
            
                if len(vanished) >= 4:
                    puyo_pop = True
                    for vi, vj in vanished:
                        field[vi][vj] = '.'
    
    if puyo_pop == True:
        puyopuyo += 1
        down(field)
    else:
        break

print(puyopuyo)
