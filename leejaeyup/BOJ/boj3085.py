'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''


N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]


def max_line_len(bd):   # 현재 보드에서 행/열 기준으로 같은 색 연속 최대 길이를 구해보는 함수.
    best = 1            # 최소 1개는 있을 거다.
    for r in range(N):  # 행 검사
        cnt = 1
        for c in range(1, N):
            if bd[r][c] == bd[r][c-1]:
                cnt += 1
            else:
                if cnt > best:
                    best = cnt
                cnt = 1
        if cnt > best:  # 마지막 구간 반영
            best = cnt
    
    for c in range(N):  # 열 검사
        cnt = 1
        for r in range(1, N):
            if bd[r][c] == bd[r-1][c]:
                cnt += 1
            else:
                if cnt > best:
                    best = cnt
                cnt = 1
        if cnt > best:
            best = cnt
    return best


answer = 1

for i in range(N):  # 모든 칸에 대해, 오른쪽/아래 이웃과 색이 다르면 바꿔보고 체크해보자.
    for j in range(N):
        if j + 1 < N and board[i][j] != board[i][j+1]:  # 오른쪽과 교환.
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            cur = max_line_len(board)
            if cur > answer:
                answer = cur
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 다시 원래대로.

        if i + 1 < N and board[i][j] != board[i+1][j]:  # 아래와 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            cur = max_line_len(board)
            if cur > answer:
                answer = cur
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 다시 원래대로.


print(answer)