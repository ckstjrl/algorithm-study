'''
# [Silver II] 연결 요소의 개수 - 11724

[문제 링크](https://www.acmicpc.net/problem/11724)

### 성능 요약

메모리: 111412 KB, 시간: 212 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 11월 20일 16:39:05

### 문제 설명

<p>방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.</p>

### 출력

 <p>첫째 줄에 연결 요소의 개수를 출력한다.</p>

'''
# 초기 설정
import sys
input = lambda: sys.stdin.readline().rstrip()

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union_find(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    elif rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    union_find(u, v)

# union-find 다 한 다음 parents 순회
cnt = 0
for i in range(1, N + 1): # 1번 부모부터 대표자 세기
    if parents[i] == i:
        cnt += 1
print(cnt)
