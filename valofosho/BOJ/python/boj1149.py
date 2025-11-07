"""
BOJ1149 - RGB거리

문제 정의
1. 각각의 집은 R, G, B로 칠할 수 있고 각각의 비용이 정해져있다.
2. 이웃한 집들끼리의 색은 겹칠 수 없다.
3. 모든 집을 겹치지 않게 칠할 때 비용이 가장 적게 드는 총 비용

로직 정의
1. 첫 집을 어떤 집을 고르느냐는 관계 없이 모든 경우를 따져주기
2. 이전 집의  컬러를 기반으로 겹치지 않는 것들을 DFS 형식으로 반복 후 최소값 반환
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def recur(i,c):
    # 전체 집을 다 칠하면 return
    if i == N-1:
        return maps[i][c]
    # costs가 존재하면 리턴
    if costs[i][c]:
        return costs[i][c]
    temp = []
    for color in [0, 1, 2]:
        if color == c:
            continue
        temp.append(recur(i+1, color) + maps[i][c])
    min_cost = min(temp)
    costs[i][c] = min_cost
    return min_cost


N = int(input().strip())

maps = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
costs = [[0] * 3 for _ in range(N)]
min_cost = min(recur(0,0), recur(0,1), recur(0,2))
print(min_cost)