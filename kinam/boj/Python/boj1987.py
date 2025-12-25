'''boj1987 알파벳
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 
(1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. 
(1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.
'''

## BFS로 풀어봤는데 BFS의 분기마다 set를 copy해서 따로 알파벳 관리를 하다보니 메모리가 터짐

import sys
# from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


R, C = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]

alpha = set() # 알파벳 넣을 세트 선언 
max_cnt = 0

di = [0, 1, 0, -1]
dj = [1, 0 ,-1, 0]

def dfs(ci, cj, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] not in alpha:
            alpha.add(arr[ni][nj]) 
            dfs(ni, nj, cnt + 1)
            alpha.remove(arr[ni][nj]) # 백트래킹

alpha.add(arr[0][0]) #처음 시작부분의 알파벳 세트에 넣어주기
dfs(0, 0, 1)
print(max_cnt)