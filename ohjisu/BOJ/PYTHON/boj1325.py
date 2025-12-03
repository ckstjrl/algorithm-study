'''
# [Silver I] 효율적인 해킹 - 1325

[문제 링크](https://www.acmicpc.net/problem/1325)

### 성능 요약

메모리: 165580 KB, 시간: 10356 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 12월 2일 22:28:23

### 문제 설명

<p>해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.</p>

<p>이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.</p>

<p>이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.</p>

### 출력

 <p>첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.</p>

'''
import sys
input  = lambda :sys.stdin.readline().rstrip()
from collections import deque


N, M = map(int, input().split())

adj_lst = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    adj_lst[b].append(a)

max_cnt = 0
result = []
for start_node in range(1, N + 1):
    cnt = 0
    q = deque([start_node])
    visited = [0] * (N + 1)
    visited[start_node] = 1
    while q:
        node = q.popleft()
        cnt += 1
        for next_node in adj_lst[node]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            q.append(next_node)
    if max_cnt < cnt:
        max_cnt = cnt
        result = [start_node]
    elif max_cnt == cnt:
        result.append(start_node)

print(*(result))