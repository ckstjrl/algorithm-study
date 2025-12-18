# BOJ 2583. 영역 구하기 / D2
'''
문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다.
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때,
K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지,
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다.
M, N, K는 모두 100 이하의 자연수이다.
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과
오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다.
둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            if arr[y][x] == 1:
                continue
            arr[y][x] = 1

visited = [[1]*N for _ in range(M)] # 색칠되지 않은 공간을 세야하고, while arr != visited: 이 조건을 사용하기 위해 방문하지 않은 곳을 1로 설정
cnt = 0 # 색칠되지 않은 공간의 개수 초기값
area_list = [] # 색칠되지 않은 각 공간의 넓이 저장 리스트
while arr != visited:
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j] == 1: # 색칠되어 있지 않고, 방문한적 없으면
                q = deque([(i, j)])
                visited[i][j] = 0 # 방문하면 0으로 변경

                area = 0 # 색칠되지 않은 각 공간의 넓이 / 밑 while문이 종료되면 한 공간의 넓이 갖게되고, 위 while문 실행시 초기화
                while q:
                    ti, tj = q.popleft()
                    area += 1 # 색칠되지 않은 칸 수 +1
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = ti + di, tj + dj
                        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 1 and arr[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 0
                area_list.append(area) # 리스트에 각 공간의 넓이 저장
                cnt += 1 # 공간의 개수 세기
area_list.sort() # 공간의 넓이 정렬
print(cnt)
print(' '.join(map(str, area_list)))

'''
1. 그림을 문제와 다르게 X축 대칭을 하여 이차원 배열에 쉽게 그릴 수 있게 변경
2. 왼쪽 아래 x, y좌표 / 오른 쪽 위 x, y 좌표를 이차원 배열에 맞게 변경할 필요가 있음
    왼쪽 아래 x, y좌표 -> 이차원 배열[y][x]
    오른쪽 위 x, y좌표 -> 이차원 배열[y-1][x-1]
    이렇게 설정 되므로 색칠하는 과정에
    for y in range(ly, ry):
        for x in range(lx, rx):
            if arr[y][x] == 1:
                continue
            arr[y][x] = 1
    자연스럽게 활용 가능
3. BFS를 활용하여 cnt는 색칠되지 않은 공간 갯수, area는 넓이, area_list는 넓이 저장
4. 특이점으로 색칠되지 않은 곳을 arr에서 0으로 표현했으므로 visited를 평소와 다른게 방문하면 1 -> 0 변경하는 방법으로 구현
'''