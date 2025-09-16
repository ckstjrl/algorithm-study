'''
# [Gold V] 트리 - 1068

[문제 링크](https://www.acmicpc.net/problem/1068)

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색

### 제출 일자

2025년 9월 17일 00:02:18

### 문제 설명

<p>트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.</p>

<p>트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.</p>

<p>예를 들어, 다음과 같은 트리가 있다고 하자.</p>

<p style="text-align: center"><img alt="" src="https://upload.acmicpc.net/560de878-d961-475e-ada4-e1f0774e5a84/-/preview/" style="width: 200px; height: 185px;"></p>

<p>현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.</p>

<p style="text-align: center"><img alt="" src="https://upload.acmicpc.net/d46ddf4e-1b82-44cc-8c90-12f76e5bf88f/-/preview/" style="width: 200px; height: 185px;"></p>

<p>이제 리프 노드의 개수는 1개이다.</p>

### 입력

 <p>첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.</p>

### 출력

 <p>첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.</p>

'''

import sys
input = sys.stdin.readline

def dfs(target, nodes) :
    # 해당 노드를 -2로 만듦
    nodes[target] = -2
    for i in range(N) :
        if nodes[i] == target : # 현재 노드를 부모로 갖는 자식 노드 찾으면
            dfs(i, nodes)       # 자식, 자식의 자식, 자식의 자식의 자식도 -2로 만듦


N = int(input())
nodes = list(map(int, input().split()))
target = int(input())
cnt = 0

dfs(target, nodes)

for i, node in enumerate(nodes) :
    if node != -2 and i not in nodes:
        cnt += 1

print(cnt)