# BOJ 1012. 유기농 배추 (D2, S2)
#--------------------------------------------------2회차 풀이
T = int(input())

for tc in range(1, T+1):
    #밭 가로 M, 세로 N, 배추 개수 K
    M, N, K = map(int, input().split()) 
    
    #빈 밭, 델타 배열 생성
    arr = [[0] * M for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for _ in range(K):
        x, y = map(int, input().split())

        # 배추 심기 (행/열 반대 유의)
        arr[y][x] = 1

    # 풀이법: 전체 밭을 순회하며 조건마다 DFS. 매 DFS마다 지렁이 cnt += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                stack = [(i,j)]
                arr[i][j] = 0   # 0 마킹으로 방문 체크 대체
                cnt += 1

                while stack:
                    ci, cj = stack.pop()
                    for k in range(4):
                        ni, nj = ci+di[k], cj+dj[k] 
                        if 0<= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                           stack.append((ni, nj)) 
                           arr[ni][nj] = 0

    print(cnt)




#--------------------------------------------------1회차 풀이

# T = int(input())
# for tc in range(1, T+1):
#     M, N, K = map(int, input().split())
    
#     # DFS 준비
#     arr = [[0] * M for _ in range(N)]
#     visited = []
#     cnt = 0

#     # 우하좌상 델타
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]

#     # 밭에 배추 표시하기
#     for _ in range(K):
#         bachu_x, bachu_y = map(int, input().split())
#         arr[bachu_y][bachu_x] = 1

#     #전체 밭을 순회하면서, 조건에 맞는 위치를 발견하면 DFS 시작
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1 and (i, j) not in visited:
#                 cnt += 1       # 지렁이 개수 추가
#                 stack = [(i, j)]
#                 visited.append((i,j))
                
#                 while stack:
#                     ci, cj = stack.pop()
#                     #### 꺼낼 때 체크 로직인데 여기서도 비지티드 체크를 해서 중복 추가 문제 발생 
#                     #### (while문 밖으로 빼서 해결 - 시작점에 대한 추가만 필요했기 때문에)

#                     for k in range(4):
#                         ni, nj = ci + di[k], cj + dj[k]
#                         if 0 <= ni < N and 0 <= nj < M:
#                             if arr[ni][nj] == 1 and (ni, nj) not in visited:
#                                 stack.append((ni, nj))
#                                 visited.append((ni, nj))
#     print(cnt)
