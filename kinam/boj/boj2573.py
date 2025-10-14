'''boj2573 - 빙산

지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자. 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 
빙산 이외의 바다에 해당되는 칸에는 0이 저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.

 	 	 	 	 	 	 
 	2	4	5	3	 	 
 	3	 	2	5	2	 
 	7	6	2	4	 	 
 	 	 	 	 	 	 
그림 1. 행의 개수가 5이고 열의 개수가 7인 2차원 배열에 저장된 빙산의 높이 정보

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 
따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다.

 	 	 	 	 	 	 
 	 	2	4	1	 	 
 	1	 	1	5	 	 
 	5	4	1	2	 	 
 	 	 	 	 	 	 
그림 2

 	 	 	 	 	 	 
 	 	 	3	 	 	 
 	 	 	 	4	 	 
 	3	2	 	 	 	 
 	 	 	 	 	 	 
그림 3

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 
그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다. 
'''
from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]



ans = 0
bingsan_cnt = 0
while True:
    visited = [[0] * M for _ in range(N)]

    if bingsan_cnt >= 2:
        break

    bingsan = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                bingsan.append((i, j))
    
    if not bingsan:
        ans = 0 #빙산 모두 녹았는데 분리가 안된 경우
        break
    
    bingsan_cnt = 0

    for ci, cj in bingsan:
        if not visited[ci][cj]:
            bingsan_cnt += 1
            q = deque([(ci, cj)])
            visited[ci][cj] = 1

            while q:
                y, x = q.popleft()
                for d in range(4):
                    ni, nj = y + di[d], x + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] > 0:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
    
    if bingsan_cnt >= 2:
        break

    #빙산 녹일 양 계산 ( 위에서 같이 진행할 경우 빙산이 녹아서 0이 되어버려 바닷물로 취급되는 경우때문에 따로 분리 )
    melt = [[0] * M for _ in range(N)]
    for ci, cj in bingsan:
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                # arr[ci][cj] -= 1 >> 순차적으로 빼면 0이 될 때 바닷물취급
                melt[ci][cj] += 1

    for ci, cj in bingsan:
        arr[ci][cj] -= melt[ci][cj]
        if arr[ci][cj] < 0:
            arr[ci][cj] = 0


    ans += 1

print(ans)