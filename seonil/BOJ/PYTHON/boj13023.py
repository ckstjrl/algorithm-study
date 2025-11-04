"""
BOJ13023. ABCDE
[문제]
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.
오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.
둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

[출력]
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.
"""
import sys
sys.setrecursionlimit(3000)  # 재귀 깊이 문제 방지

def dfs(v, depth): # 현재 노드 v, 깊이 depth

    global relationExists
    if depth == 4:  # 깊이 4 → 정점 5개 연결됨
        relationExists = True
        return

    visited[v] = True  # 현재 정점 방문 처리
    for w in relations[v]:
        if not visited[w]: # 인접 노드 w에 대하여
            dfs(w, depth + 1)
            visited[w] = False  # 백트래킹: 다른 경로 탐색 위해 방문 해제

# main
input = sys.stdin.readline
N, M = map(int, input().split())
relations = [[] for _ in range(N)]  # 인접 리스트
visited = [False] * N
relationExists = False  # 조건을 만족하는 친구 관계가 존재하는지 여부

# 입력으로 무방향 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a) # 무방향 간선 그래프

# 모든 정점에서 DFS 시작
for i in range(N):
    dfs(i, 0)
    visited[i] = False  # 초기화
    if relationExists:  # 관계 존재 확인 시 검사 종료
        break

# 결과 출력
print(1 if relationExists else 0)