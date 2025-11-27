# BOJ 1774. 우주신과의 교감 / D3
'''
빵상!
빵 빵 똥 똥 똥 똥 땅 땅 따라라라~ 따띵 똥 똥 똥 똥 띵똥똥

문제
황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.

하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.

우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.

또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.

이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

입력
첫째 줄에 우주신들의 개수 N, 이미 연결된 신들과의 통로의 개수 M가 주어진다.
두 번째 줄부터  N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 X, Y가 주어진다.
그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다.
번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

출력
첫째 줄에 만들어야 할 최소의 통로 길이를 소수점 둘째 자리까지 반올림하여 출력하라.
'''
import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry: # 사이클 발생
        return

    # 일정한 규칙으로 병합 (더 작은 수로)
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

N, M = map(int, input().split())
alien_axis = [0]
for _ in range(N):
    x, y = map(int, input().split())
    alien_axis.append((x, y))

graph = [(0, 0, 0)] # 0 index를 안쓰기위함

# 각 행성들 간의 거리 계산해서 graph에 연결된 간선과 비용으로 넣어줌
for i in range(1, N+1):
    for j in range(i+1, N+1):
        x1, y1 = alien_axis[i][0], alien_axis[i][1]
        x2, y2 = alien_axis[j][0], alien_axis[j][1]
        c = ((abs(x1-x2))**2 + (abs(y1-y2))**2)**(1/2)
        graph.append((i, j, c))

# 이미 연결된 노드 같은 경우 간선 비용을 0으로 설정
# 이렇게 하면 위에서 간선 비용을 넣어줬더라도 최소비용을 구하는 알고리즘이므로
# 비용이 0인 간선 비용만 사용됨
for _ in range(M):
    c_1, c_2 = map(int, input().split())
    graph.append((c_1, c_2, 0))

parents = [i for i in range(N+2)]

graph.sort(key=lambda x: x[2])

cnt = 0 # 현재까지 선택한 간선의 수
result = 0 # 비용

# 연결 간선 수가 노드-1이 될 때까지 진행
for u, v, w in graph:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == N-1:
            break
print(f"{result:.2f}")

'''
최소신장트리 - kruskal 알고리즘 활용
'''