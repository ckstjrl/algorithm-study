'''
백준 25558 내비게이션 

[문제]

- 시작점 (s_x, s_y)와 도착점 (e_x, e_y) 
- 각 내비게이션의 시작점 (s_x, s_y)에서 도착점 (e_x, e_y)$지 도달하기 위해서 순차적으로 방문해야 하는 중간 지점들의 위치
두 지점 간의 거리는 맨해튼 거리로 정의된다. 즉, (a,b)와 (c,d)와의 거리는 |a-c|+|b-d|이다. 
그리고 각 내비게이션이 안내한 목적지까지의 최적 경로의 거리는 서로 다르다.

그러나 SUAPC 2022 Summer 대회 당일에 컴퓨터의 갑작스러운 고장으로 인해 각 내비게이션에 대한 실험값들이 서로 뒤바뀌었다.
대회가 끝나기 전에 각 내비게이션의 데이터가 주어졌을 때, 어느 데이터가 OEM 순정 내비게이션인지 찾아보자.

[입력]
첫 번째 줄에 실험에 사용한 내비게이션의 개수를 의미하는 양의 정수 N이 주어진다. 
(2 <= N <= 1000)

두 번째 줄에 시작점과 도착점의 좌푯값을 의미하는 s_x, s_y,e_x, e_y를 의미하는 네 정수가 공백으로 구분되어 주어진다.
그다음 줄에는 1번 내비게이션부터 N번 내비게이션의 데이터에 대한 입력이 순차적으로 주어진다. 각 내비게이션에 대한 입력은 다음과 같이 주어진다.

[출력]
OEM 순정 내비게이션에 해당하는 데이터 번호를 출력하여라.
'''
# 네비게이션이 안내한 경로의 총 거릴를 맨해튼 거리로 치환하고 
# 그 중에서 가장 짧은 거리를 가진 네비게이션 번호 찾기

# 거리 계산 함수 입력 
def manhattan(x1, y1, x2, y2):
    # 두 점 사이의 맨해튼 거리 계산
    return abs(x1 - x2) + abs(y1 - y2)

N = int(input().strip())  # 내비게이션 개수

# 시작점, 도착점 입력 
sx, sy, ex, ey = map(int, input().split()) 

best_road = None   # 가장 짧은 거리
best_nav = -1      # 짧은 거리 내비게이션 번호

for nav in range(1, N + 1):
    M = int(input().strip())  # 내비의 중간 지점 개수

    points = []
    for _ in range(M):
        x, y = map(int, input().split())
        points.append((x, y))

    # 거리 계산 
    total = 0

    # 시작점 → 첫 번째 중간 지점
    px, py = sx, sy
    for x, y in points:
        total += manhattan(px, py, x, y)
        px, py = x, y

    # 마지막 중간 지점 → 도착점
    total += manhattan(px, py, ex, ey)

    # 가장 짧은 경로인지 확인
    if best_road is None or total < best_road:
        best_road = total
        best_nav = nav

print(best_nav)
