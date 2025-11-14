'''
# [Silver II] 결혼식 - 5567

[문제 링크](https://www.acmicpc.net/problem/5567)

### 성능 요약

메모리: 110720 KB, 시간: 108 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2025년 11월 12일 00:35:12

### 문제 설명

<p>상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.</p>

<p>상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 a<sub>i</sub> b<sub>i</sub>가 주어진다. (1 ≤ a<sub>i</sub> < b<sub>i</sub> ≤ n) a<sub>i</sub>와 b<sub>i</sub>가 친구라는 뜻이며, b<sub>i</sub>와 a<sub>i</sub>도 친구관계이다. </p>

### 출력

 <p>첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.</p>

'''
# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

def dfs(now, length):
    if dist[now] < length: # 가지치기
        return

    dist[now] = length # 가지치기에 해당하지 않을 때 업데이트

    if length > 2: # 종료조건: 친구의 친구보다 더 멀어지면 종료
        return

    for next in graph[now]: # 현재 인접 리스트에 해당하는 친구 목록 순회
        dfs(next, length + 1) # 현재 인접 리스트에 해당하는 친구1 재귀 호출

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
invite = set()
dist = [float('inf')] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

cnt = 0
for i in range(2, N + 1): # 상근이 제외하고 거리 cnt
    if 0 < dist[i] <= 2:
        cnt += 1

print(cnt)