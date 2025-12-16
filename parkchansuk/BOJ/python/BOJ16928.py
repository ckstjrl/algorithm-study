# BOJ 16938. 뱀과 사다리 게임
'''
게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다.
게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다.
보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다.
예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다.
만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.
뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고,
뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.
'''
import sys
from collections import deque
stage = {}
N, M = map(int, sys.stdin.readline().split())

for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().split())
    stage[x] = y

q = deque([[1,0]])
visited = [0]*101
visited[1] = 1
while q:
    i, cnt = q.popleft()
    if i == 100:
        print(cnt)
        break

    for a in range(1, 7):
        nxt = i+a
        if nxt <= 100:
            if nxt in stage:
                nxt = stage[nxt]
            if visited[nxt] != 1:
                visited[nxt] =1
                q.append([nxt, cnt+1])

'''
BFS 활용하는 문제
깜빡하고 visited 처리 안해줬다가 메모리 초과 발생
뱀과 사다리를 굳이 구분해 줄 필요 없음
전부다 stage dict에 시작점을 key로 도착점을 value로 받아서 처리함
(아마 list 안에 list나 튜플로 받아서 처리도 가능할 듯)
현재 위치와 몇 번 주사위를 굴렸는지 덱에 넣고 빼고 반복하여
현재 위치가 100에 도착하면 while문을 나오면서 cnt 출력
'''