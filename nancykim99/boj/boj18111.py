'''
BOJ18111. 마인크래프트
세로 N, 가로 M의 집터 -> 0,0부터 시작
B : 인벤토리에 들어있는 블록 수

1. i, j의 가장 위에 있는 블록을 제거하여 인벤토리에 넣기 -> 2초
2. 인벤토리에서 블록 하나를 꺼내어 i, j의 가장 위에 놓기 -> 1초

최소 시간과 높이 출력하기

해결 방법 : 그냥 0부터 256층까지 완전탐색해서 해결함
'''
import sys

N, M, B = map(int,sys.stdin.readline().split())

block = []
for _ in range(N):
    block.append(list(map(int,sys.stdin.readline().split())))

ans = 21e8
height = 0

for i in range(257):
    used_block = 0
    digged_block = 0
    
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                digged_block += block[x][y] - i
            else:
                used_block += i - block[x][y]

    if used_block > digged_block + B:
        continue

    cnt = digged_block * 2 + used_block

    if cnt <= ans:
        ans = cnt
        height = i 

print(ans, height)