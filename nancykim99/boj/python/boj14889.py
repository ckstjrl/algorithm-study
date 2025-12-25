'''
BOJ14889 : 스타트와 링크

해결 방법 : 조합을 구하고, 조합을 다 구했으면, 두 조합의 차를 ans에 더 작은 값만 업데이트
'''

import sys
input = sys.stdin.readline

def find_least_diff(cnt, idx):
    global ans, n
    if cnt == n // 2: 
        start, link = 0, 0
        for i in range(n-1):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += graph[i][j] + graph[j][i]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j] + graph[j][i]
        ans = min(ans, abs(start - link))

    else: 
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = 1
                find_least_diff(cnt+1, i+1)
                visited[i] = 0
    return ans

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
ans = float('inf')
print(find_least_diff(0, 0))