'''
문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.
'''



# 생각보다 꽤 어렵다. 못 풀겠다.
# 이렇게 푸는 문제였구나...
# BOJ 13023 ABCDE - 가장 쉬운 DFS 버전

N, M = map(int, input().split())

# 친구 관계(무방향 그래프)를 인접 리스트로 저장
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * N

def dfs(u, depth):
    """
    u: 현재 사람(정점)
    depth: 지금까지 이어진 사람 수 (u를 포함)
    목표: depth가 5가 되면 A-B-C-D-E 완성
    """
    if depth == 5:          # 서로 다른 5명 연결 성공
        return True

    visited[u] = True
    for v in adj[u]:
        if not visited[v]:              # 아직 방문 안 한 사람만 이어 붙이기
            if dfs(v, depth + 1):       # 하나라도 성공하면 곧장 True 전파
                return True
    visited[u] = False                   # 백트래킹(다른 시작점에서 다시 쓸 수 있게 해제)
    return False

# 모든 사람을 시작점으로 시도
for i in range(N):
    if dfs(i, 1):            # i 혼자로 시작하니 depth=1
        print(1)
        break
else:
    print(0)

    '''
    가능한 한 간단하게—“길이가 5인 사람 연쇄(서로 다른 5명)”가 있는지만 재귀 DFS로 확인하면 됩니다.
    핵심은 현재까지 몇 명을 연결했는지(depth) 를 세다가 5명이 되면 성공을 True로 바로 반환하는 것!

	“5명이 이어지면 True”라는 한 가지 조건만 보고 바로 빠져나옵니다.
	•	visited는 서로 다른 사람만 연속 방문하도록 보장합니다.
	•	실패하면 False를 리턴하면서 자연스럽게 다른 경로를 시도합니다.

    이 버전은 플래그 전역 변수도 없고, 로직 흐름이 “맞으면 True 반환”이라 초보자도 따라가기 편해요.
    '''