'''
# [Silver II] 사탕 게임 - 3085

[문제 링크](https://www.acmicpc.net/problem/3085)

### 성능 요약

메모리: 112016 KB, 시간: 568 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 9월 30일 16:20:58

### 문제 설명

<p>상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.</p>

<p>가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.</p>

<p>사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)</p>

<p>다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.</p>

<p>사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.</p>

### 출력

 <p>첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.</p>

'''
import sys
input = lambda : sys.stdin.readline().rstrip()

DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def find() :
    max_len = 1
    # 모든 행을 검사
    for i in range(N):
        count = 1
        for j in range(N - 1):
            if graph[i][j] == graph[i][j + 1]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)

    # 모든 열을 검사
    for j in range(N):
        count = 1
        for i in range(N - 1):
            if graph[i][j] == graph[i + 1][j]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)
    return max_len


N = int(input())

graph = [list(input()) for _ in range(N)]

max_sum = 0

for i in range(N) :
    for j in range(N) :
        now_color = graph[i][j]
        for di, dj in DIRS :
           ni, nj = i + di, j + dj
           if not (0 <= ni < N and 0 <= nj < N) :
               continue
           if graph[ni][nj] == now_color :
               continue
           graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
           now_sum = find()
           max_sum = max(max_sum, now_sum)
           graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
print(max_sum)