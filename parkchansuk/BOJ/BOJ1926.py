# BOJ 1926. 그림 / D2
'''
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다.
그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라.
단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0 # 그림의 개수 초기값
max_area = 0 # 넓이의 최댓값 초기값
while graph != visited:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                q = deque([(i, j)])
                visited[i][j] = 1

                area = 0 # 그림의 넓이
                while q:
                    y, x = q.popleft()
                    area += 1 # 하나 뽑힐때마다 넓이 1씩 추가된다
                    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and graph[ny][nx] == 1:
                            q.append((ny, nx))
                            visited[ny][nx] = 1
                if area > max_area:
                    max_area = area # 최종적으로 while문이 끝나면 그림 하나의 넓이가 나오고 최댓값과 비교하여 교체

                cnt += 1 # while문 반복되는 만큼 그림의 수

print(cnt)
print(max_area)

'''
BFS 사용함
첫번째 while문은 그래프와 visited가 동일해지면 완전 탐색을 끝내는 역할을 진행
그 안에서 방문하지 않은 그래프 1을 찾아 시작점으로 설정
두번째 while문은 하나의 그림을 탐색하는 역할을 함
두번째 while문 내부에서 pop 반복된 횟수 = 그림의 넓이
첫번째 while문 내부에서 두번째 while문이 진행된 횟수 = 그림의 개수
이렇게 생각하고 풀이 진행
(참고 : 유기농 배추 문제와 유사)
'''