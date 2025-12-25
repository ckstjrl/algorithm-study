# 1063. 킹

import sys
input = sys.stdin.readline

col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']      # 열 숫자 - 알파벳 대응을 위한 리스트

# 입력 명령어별 이동 
moves = {     
    'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
}

k_pos, s_pos, n = input().split()   
kx, ky = col.index(k_pos[0])+1, int(k_pos[1])   # 킹의 위치
sx, sy = col.index(s_pos[0])+1, int(s_pos[1])   # 돌의 위치 
n = int(n)

for _ in range(n):
    cmd = input().rstrip()  # 입력 명령어
    temp_x, temp_y = kx+moves[cmd][0], ky+moves[cmd][1]     # 임시 킹 좌표 (명령어대로 이동)
    temp_sx, temp_sy = sx, sy                               # 임시 돌 좌표 
    if (temp_x, temp_y) == (sx, sy):    # 만약 임시 킹 좌표가 현재 돌 좌표와 같다면
        temp_sx, temp_sy = sx+moves[cmd][0], sy+moves[cmd][1]   # 임시 돌 좌표도 같은 방향으로 이동

    # 좌표 중 하나라도 체스판 범위 넘어가면 반영하지 않음
    if not (0<temp_x<=8 and 0<temp_y<=8 and 0<temp_sx<=8 and 0<temp_sy<=8):     
        continue    
    kx, ky = temp_x, temp_y
    sx, sy = temp_sx, temp_sy

# 형식에 맞게 출력 
print(col[kx-1] + str(ky))
print(col[sx-1] + str(sy))
