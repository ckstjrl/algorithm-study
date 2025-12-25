'''boj7576 
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지,
그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''


# def has_0(arr):
#     return any(0 in x for x in arr)


# import sys
# from collections import deque
# input = sys.stdin.readline  #input을 sys.stdin.readline으로 치환

# M, N = map(int, input().split())
# tomatos = [list(map(int, input().split())) for _ in range(N)]

# if not has_0(tomatos):
#     print(0)

# else:
#     q = deque([])
#     visited = [[0] * M for _ in range(N)]

#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]

#     date = -1

#     for i in range(N):
#         for j in range(M):
#             if tomatos[i][j] == 1:  #익은 토마토(시작점)이면 큐에 추가하고 방문표시
#                 q.append([i, j])
#                 visited[i][j] = 1

#     while q:
#         ci, cj = q.popleft()

#         # if not has_0(tomatos):  #0이 없게 되면?
#         #     date = visited[ci][cj] - 1
            

#         for ni, nj in zip(di, dj):
#             fi, fj = ci + ni, cj + nj
#             # 다음 인덱스가 배열 벗어나지 않고 and 안익은 토마토고 and 방문하지 않은 곳이면
#             if 0 <= fi < N and 0 <= fj < M and tomatos[fi][fj] == 0 and not visited[fi][fj]:
#                 visited[fi][fj] = visited[ci][cj] + 1   #방문 표시해주되 날짜 정보도 같이 넣기. 날짜 +1일 된거임
#                 q.append([fi, fj]) 
#                 tomatos[fi][fj] = 1 #0은 안익은 토마토니까 1로 재할당해줘서 익은 토마토표시

#                 if not has_0(tomatos):
#                     date = visited[ci][cj]
#                     break
        
#         if date != -1:
#             break

#     print(date)
            

################################################################
#has_0함수가 시간복잡도 큰 듯 시간초과남


# sys로 잔재주를 부려선 안될 것
# import sys
from collections import deque
# input = sys.stdin.readline  #input을 sys.stdin.readline으로 치환

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]


q = deque([])
visited = [[0] * M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

date = -1
tomato_0 = 0    #안익은 토마토 개수

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:  #익은 토마토(시작점)이면 큐에 추가하고 방문표시
            q.append([i, j])
            visited[i][j] = 1

        elif tomatos[i][j] == 0:   #안익은 토마토면 안익은 토마토 개수 증가
            tomato_0 += 1

if tomato_0 == 0:   #시작부터 안익은 토마토 없으면
    print(0)

else:
    while q:
        ci, cj = q.popleft()

        for ni, nj in zip(di, dj):
            fi, fj = ci + ni, cj + nj
            # 다음 인덱스가 배열 벗어나지 않고 and 안익은 토마토고 and 방문하지 않은 곳이면
            if 0 <= fi < N and 0 <= fj < M and tomatos[fi][fj] == 0 and not visited[fi][fj]:
                visited[fi][fj] = visited[ci][cj] + 1   #방문 표시해주되 날짜 정보도 같이 넣기. 날짜 +1일 된거임
                q.append([fi, fj]) 
                tomatos[fi][fj] = 1 #0은 안익은 토마토니까 1로 재할당해줘서 익은 토마토표시
                tomato_0 -= 1   #안익은토마토 익었으니까 1 빼줌

            if tomato_0 == 0:
                date = visited[ci][cj]
                break

        if tomato_0 == 0:
            break

    print(date)