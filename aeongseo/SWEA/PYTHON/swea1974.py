'''
1974. 스도쿠 검증 (D2)

스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1부터 9까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1에서 9까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1에서 9까지의 숫자가 겹치지 않아야 한다.
입력으로 9 x 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0을 출력한다.
'''

def sudoku_col(arr):
    # 행 우선순회
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[arr[i][j]-1] += 1   # 칸에 적힌 값에 해당하는 카운트 증가
        if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] == cnt[5] == cnt[6] == cnt[7] == cnt[8] : # 겹치는 수 없으면 순회 계속 진행
            continue
        else:
            return 0    # 겹치는 수가 있으면 순회 중단, 0 반환
    return 1            # 모든 행에서 겹치는 수가 없다면 1 반환

def sudoku_row(arr):
    # 열 우선순회
    for j in range(9):
        cnt = [0] * 9
        for i in range(9):
            cnt[arr[i][j]-1] += 1   # 칸에 적힌 값에 해당하는 카운트 증가
        if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] == cnt[5] == cnt[6] == cnt[7] == cnt[8] : # 겹치는 수 없으면 순회 계속 진행
            continue
        else:
            return 0    # 겹치는 수가 있으면 순회 중단, 0 반환
    return 1            # 모든 행에서 겹치는 수가 없다면 1 반환

def sudoku_box(arr):
    # 3x3칸 순회
    for i in range(0, 9, 3):    # 3x3범위의 외쪽 모서리 칸으로 도착해야 하므로 인덱스 3칸씩 건너뛰어 접근
        for j in range(0, 9, 3):
            cnt = [0] * 9
            for d1 in range(i, i+3):
                for d2 in range(j, j+3):
                    cnt[arr[d1][d2]-1] += 1 # 칸에 적힌 값에 해당하는 카운트 증가
            if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] == cnt[5] == cnt[6] == cnt[7] == cnt[8]:  # 겹치는 수 없으면 순회 계속 진행
                continue
            else:
                return 0    # 겹치는 수가 있으면 순회 중단, 0 반환
    return 1                # 모든 행에서 겹치는 수가 없다면 1 반환

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    col = sudoku_col(arr)
    row = sudoku_row(arr)
    box = sudoku_box(arr)

    if col == 1 and row == 1 and box == 1:  # 모든 행, 열, 3x3에서 1이 반환되었다면 1 출력
        print(f'#{tc} 1')
    else:                                   # 하나라도 0이 반환되었다면 0 출력
        print(f'#{tc} 0')