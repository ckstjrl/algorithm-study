'''
# [Gold V] ABCDE - 13023 

[문제 링크](https://www.acmicpc.net/problem/13023) 

### 성능 요약

메모리: 112164 KB, 시간: 472 ms

### 분류

그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹

### 제출 일자

2025년 9월 4일 22:40:54

### 문제 설명

<p>BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.</p>

<p>오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.</p>

<ul>
	<li>A는 B와 친구다.</li>
	<li>B는 C와 친구다.</li>
	<li>C는 D와 친구다.</li>
	<li>D는 E와 친구다.</li>
</ul>

<p>위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.</p>

### 출력 

 <p>문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.</p>




'''



import sys
sys.stdin = open("./algorithm-study/test.txt", "r")
input = sys.stdin.readline

def f(a, cnt) : # a: 친구1 인덱스, cnt: 연결된 인원 수
    if cnt == 4 : return True # 4명이 연결되면 종료
    for b in adj[a] : # a 친구들 탐색
        if not visited[b] : # a 친구들 중에 확인 안한 애가 있으면
            visited[b] = True # 방문 표시
            if f(b, cnt + 1) : return True # a 친구 b 확인하기
            visited[b] = False # 통과 못하면 방문표시 초기화
    return False # 다 돌았는데도 못찾으면 False 반환

N, M = map(int, input().split())

adj = [[] for _ in range(N)] # 인접 리스트 생성

for i in range(M) : # 간선 수 만큼
    a, b = map(int, input().split()) 
    adj[a].append(b) # 양방향으로 저장
    adj[b].append(a)

visited = [0] * N # N개 만큼 방문 표시 위함
flag = 0 # 잘 찾았는지 확인
for i in range(N) : # 인접리스트 순회 및 방문 표시를 위한 i
    visited[i] = True # 방문 표시
    if f(i, 0) == True : # cnt == 4인걸 찾으면
        print(1)         # print(1) 찍고 종료
        flag = 1
        break
    visited[i] = False   # 아니면 다음거 탐색을 위해 visited 초기화
if not flag : print(0) # 잘 못찾았으면 print(0)