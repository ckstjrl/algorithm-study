'''boj14500

폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
'''
# ㅗ ㅏ ㅜ 모양 어캐 만듦?
# 백트래킹 해서 가야 만들 수 있을듯
# bfs 재귀로 만들고 visited 이용해서 백트래킹하기

#해보니까 ㅗㅜㅏㅓ 백트래킹으로 안댈듯
# 따로 추가하기



def bfs(ci, cj, sum, cnt):
    global max_sum

    if cnt == 4:    #테트로미노 완성이면? 최댓값 갱신
        if max_sum < sum:
            max_sum = sum
        return
    
    for ni, nj in zip(di, dj):
        fi, fj = ci + ni, cj + nj
        if 0 <= fi < N and 0 <= fj < M and visited[fi][fj] == 0:
            visited[fi][fj] = 1
            bfs(fi, fj, sum + arr[fi][fj], cnt + 1)
            visited[fi][fj] = 0


N, M = map(int, input().split()) #세로 크기 N 가로 크기 M
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
#시작점의 i, j , sum, 카운트
max_sum = 0

for i in range(N):
    for j in range(M):
        # ㅗ 모양
        if i+1 < N and j-1 >= 0 and j+1 < M:
            t_sum = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j]
            max_sum = max(max_sum, t_sum)
        
        # ㅜ 모양
        if i-1 >= 0 and j-1 >= 0 and j+1 < M:
            t_sum = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i-1][j]
            max_sum = max(max_sum, t_sum)
        
        # ㅏ 모양
        if i-1 >= 0 and i+1 < N and j+1 < M:
            t_sum = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j+1]
            max_sum = max(max_sum, t_sum)
        
        # ㅓ 모양 
        if i-1 >= 0 and i+1 < N and j-1 >= 0:
            t_sum = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1]
            max_sum = max(max_sum, t_sum)
            
        visited[i][j] = 1
        bfs(i, j, arr[i][j], 1)
        visited[i][j] = 0

        


print(max_sum)



