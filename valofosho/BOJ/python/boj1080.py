"""
BOJ 1080 - 행렬
문제 정의
1. NXM 행렬 두 개가 주어지고, 첫 행렬을 두 번째 행렬과 동일하게 만드는 횟수를 구하라
2. 행렬은 0, 1 로 이루어져 있고, 3x3 행렬을 뒤집는 연산만 가능하다.

로직 정의
1. 3x3 행렬로만 뒤집는게 가능하다는 점은 인덱스의 범위를 0~N-2, 0~M-2까지 그리디하게 돌릴 수 있다는 것
2. 전체 행렬을 순회해야하는데 이유는 한 점만 바꾸는게 불가능해 하나의 점을 바꾸고 이를 제외한 나머지에 대한 지속적인 순회 필요
3. 전체를 다 순회한 뒤 바꾸는 횟수인 cnt를 출력한다.
4. 단 순회가 모두 종료되었을 때, 1번 행렬과 2번 행렬의 요소 중 하나라도 다르다면 -1을 출력한다.
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
asis = [list(map(int, input().strip())) for _ in range(N)]
tobe= [list(map(int, input().strip())) for _ in range(N)]
cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if asis[i][j] != tobe[i][j]:
            cnt += 1
            for x in range (i,i+3):
                for y in range(j, j+3):
                    if asis[x][y] == 1:
                        asis[x][y] = 0
                    else:
                        asis[x][y] = 1
flag = False
for i in range(N):
    for j in range(M):        
        if asis[i][j] != tobe[i][j]:
            flag = True
            break
    if flag:
        break
print(-1 if flag else cnt)