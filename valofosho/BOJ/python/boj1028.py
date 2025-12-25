"""
BOJ1028 - 다이아몬드 광산

문제 정의
다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하라
다이아몬드는 1이 마름모로 이어져있어야 한다.

로직 정의
처음에는 BFS의 형식을 떠올렸는데 시간 초과 수준이 아니라 시간 폭발이 예상됨
-> DP 테이블로 꾸려보기
1. 좌측상단부터 행을 탐색한다.
2. 탐색은 기존의 좌우가 아닌 대각을 기준으로 한다.
3. 한 지점(상단 꼭짓점) 기준 다이아몬드가 생기는건 
    a. 좌하단, 우하단이 l만큼 있다고 가정했을 때,
    b. l만큼 아래로 반대로 꺾여있는 만큼 있어야 다이아몬드
4. DP 테이블을 4개를 만들어 좌하단, 좌상단, 우하단, 우상단을 각각 담아둔다.
5. 특정 꼭짓점이 1이면 거기서 다이아가 만들어지는지 확인!

메모
1. 이런 문제(배열의 이동이나 현재 범위 체크가 아닌 더 나아간 체크)에서는 패딩이 유리하다
"""


import sys
input = sys.stdin.readline

R, C = map(int, input().split())
# 범위 체크를 피하기 위한 패딩
maps = [[0] * (C+2) for _ in range(R+2)]
for i in range(1, R+1):
    s = input()
    for j in range(1, C+1):
        maps[i][j] = int(s[j-1])
# 각각 좌하단, 우하단, 좌상단, 우상단 대각선의 길이를 담을 DP배열
ld = [[0]* (C+2) for _ in range(R+2)]
rd = [[0]* (C+2) for _ in range(R+2)]
lu = [[0]* (C+2) for _ in range(R+2)]
ru = [[0]* (C+2) for _ in range(R+2)]

for i in range(R, 0, -1):
    for j in range(1, C+1):
        # 하단 값들은 아래에서부터 위로 순회하며 DP테이블 채우기
        if maps[i][j] == 1:
            ld[i][j] = ld[i+1][j-1] + 1
            rd[i][j] = rd[i+1][j+1] + 1
for i in range(1, R+1):
    for j in range(1, C+1):
        if maps[i][j] == 1:
        # 상단 값들은 기존 순회와 동일한 방식으로 순회하며 채우기
            lu[i][j] = lu[i-1][j-1] + 1
            ru[i][j] = ru[i-1][j+1] + 1

ans = 0
for i in range(1, R+1):
    for j in range(1, C+1):
        # 좌하단, 우하단 대각선의 최소값을 구해, 해당 범위까지 가능한 다이아 크기 찾기
        for k in range(ans + 1, min(ld[i][j], rd[i][j]) + 1):
            # 다이아몬드의 하단 꼭짓점
            bi = i + 2*(k-1)
            # 하단 꼭짓점이 범위 내라면
            if bi <= R:
                # k만큼의 범위가 되는지 확인 후
                if min(lu[bi][j], ru[bi][j]) >= k:
                    ans = k
print(ans)