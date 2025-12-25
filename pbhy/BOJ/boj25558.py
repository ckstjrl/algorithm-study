# 25558. 내비게이션
'''
OEM 순정 내비게이션이 다른 내비게이션보다 더 효율적인 목적지까지의 최적 경로를 탐색하는 것을 확인할 수 있었다.
실험 데이터는 다음과 같은 정보들을 담고 있다.
- 시작점 (s_x, s_y)와 도착점 (e_x, e_y)
- 각 내비게이션의 시작점 (s_x, s_y)에서 도착점 (e_x, e_y)까지 도달하기 위해서 순차적으로 방문해야 하는 중간 지점들의 위치
두 지점 간의 거리는 맨해튼 거리로 정의된다. 즉, (a,b)와 (c,d)와의 거리는 |a-c|+|b-d|이다.
대회가 끝나기 전에 각 내비게이션의 데이터가 주어졌을 때, 어느 데이터가 OEM 순정 내비게이션인지 찾아보자.

[입력]
첫 번째 줄에 실험에 사용한 내비게이션의 개수를 의미하는 양의 정수 N이 주어진다
두 번째 줄에 시작점과 도착점의 좌푯값을 의미하는 s_x, s_y, e_x, e_y를 의미하는 네 정수가 공백으로 구분되어 주어진다.
그다음 줄에는 1번 내비게이션부터 N번 내비게이션의 데이터에 대한 입력이 순차적으로 주어진다.
- 첫 번째 줄에는 순차적으로 방문해야 하는 중간 지점들의 위치의 개수인 M_i가 주어진다.
- 두 번째 줄부터 M_i개의 줄에 걸쳐서 j번째로 방문해야 하는 중간 지점 x좌표와 y좌표의 값을 의미하는 두 정수가 공백으로 구분되어 주어진다.

[출력]
OEM 순정 내비게이션에 해당하는 데이터 번호를 출력하여라.

거리를 다 더해서 거리가 가장 작은 수를 찾아라.
점을 모두 리스트에 담아서 for문 돌면서 계산한다.
최소 거리 갱신하면서 진행
'''
n = int(input())
s_x, s_y, e_x, e_y = map(int, input().split())
min_d = float('inf')
min_n = 0
for nc in range(1, n+1):
    m = int(input())
    points = [(s_x, s_y)]
    for i in range(m):
        m_x, m_y = map(int, input().split())
        points.append((m_x, m_y))
    points.append((e_x, e_y))
    total_distance = 0
    for j in range(len(points) - 1):
        total_distance += abs(points[j][0] - points[j + 1][0]) + abs(points[j][1] - points[j + 1][1])
    if total_distance < min_d:
        min_d = total_distance
        min_n = nc
print(min_n)