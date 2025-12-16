# BOJ 1063. 킹 / D2
'''
문제
8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다.
열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.
킹은 다음과 같이 움직일 수 있다.

R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로

킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

출력
첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.
'''
import sys
input = sys.stdin.readline

move = {"R":(1, 0), "L":(-1, 0), "B":(0, -1), "T":(0, 1), "RT":(1, 1), "LT":(-1, 1), "RB":(1, -1), "LB":(-1, -1)}

def pad_to_xy(p): # 체스판 좌표를 이차원 배열의 인덱스로
    return ord(p[0]) - ord('A'), int(p[1]) -1

def xy_to_pad(x, y): # 이차원 배열 인덱스를 체스판 좌표로
    return chr(x + ord('A')) + str(y + 1)

king, stone, N = input().split()
N = int(N)
kx, ky = pad_to_xy(king)
sx, sy = pad_to_xy(stone)

for _ in range(N):
    m = input().strip()
    dx, dy = move[m]
    nkx, nky = kx + dx, ky + dy

    # 킹이 판 안에 있는지 체크
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    # 돌과 충돌하는 경우
    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy

        # 돌이 판 안에 있는지 체크
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue

        # 돌이 판 안에 있으면 둘다 이동
        kx, ky = nkx, nky
        sx, sy = nsx, nsy

    else:
        kx, ky = nkx, nky

print(xy_to_pad(kx, ky))
print(xy_to_pad(sx, sy))

'''
체스판 좌표를 이차원배열로 바꾸고
움직임 입력을 미리 move dict에 먼저 정의해 놓음

킹을 움직이면서
킹이 판 밖으로 나가면 pass
돌이 판 밖으로 나가면 pass
돌과 충돌하는 경우 돌도 같이 움직임
돌과 충돌하지도 않고 판 밖으로 나가지도 않으면 킹만 움직임

킹의 좌표를 다시 체스판 좌표로 변경하여 출력
'''