"""
문제 정의
1. 9x9 스도쿠 판에 비어있는 칸은 0으로 입력이 주어진다.
2. 모든 빈 칸은 스도쿠 규칙을 만족하는 숫자로 채워지는 경우의 수가 존재한다.
3. 모든 빈 칸이 채워진 최종 모습을 출력하라

로직 고민
1. 스도쿠의 기본 규칙
    - 3x3 정사각 배열은 0~9의 값이 각 하나씩 들어간다
    - 각 행, 열은 모두 0~9의 값이 하나씩 들어간다.
    - 만약 모든 빈 칸이 들어갈 수 있는 경우의 수가 하나가 아니라면
        -> 그 중 하나를 선택하고 이 경우의 수가 가능한 경우의 수인지 차례대로 값을 넣어가면서 확인

2. 이 문제의 핵심은 백트래킹으로 시간을 단축하는 것
    - 빈칸에 어떤 수가 들어갔을 때 불가능한 경우가 존재한다.
    - 이 핵심 로직을 어떻게 풀어내느냐

3. 만약 모든 빈칸 중 하나의 빈칸에 반드시 하나의 값만 경우의 수가 되는 경우가 있다면 좋겠지만 아닐듯
    - 각 빈칸에 들어갈 수 있는 후보군이 존재할테고
    - 어떤 빈칸을 우선순위로 채워나갈 것인가
    - 인간은 참 똑똑해


로직 정의
1. 스도쿠 판의 배열은 9x9 
2. 우선 빈 칸에 들어갈 수 있는 무언가를 정의?
3. 초기 값을 먼저 찾아보자
    - 우선 하나하나 탐색하는 것 보다 한 블럭씩 돌아가면서 정의하는게 빠를듯
    - 이유는 만약 하나하나 탐색하면 같은 3x3 블럭 탐색을 반복하는 경우가 생김
    - 아니면 아예 3x3 블럭을 리스트로 담아서 넣을 수 있는 값을 담은 리스트를 두는건?
        -> [1, 2, 3, 4, 5, 6, 7, 8, 9] 이렇게 번호로? 담아두기?
        
완탐으로 풀고 고쳐보자
"""

import sys
input = sys.stdin.readline

# 같은 행에 있으면 False 없어야 True
def check_row(i, j, x):
    if x in board[i]:
        return False
    else:
        return True

# 같은 열에 있으면 False
def check_col(i, j, x):
    for r in range(9):
        if board[r][j] == x:
            return False
    else:
        return True
    
# 베이스에 들어있어야 True
def check_box(i, j, x):
    if x in base[i//3][j//3]:
        return True
    else:
        return False


def sudoku():
    if not stack:
        return True
    i,j = stack.pop()
    # 0 자리에 들어갈 수 있는 후보군(3x3 박스 기준)
    cands =  set(base[i//3][j//3])
    for x in cands:
        if check_row(i,j,x) and check_col(i,j,x) and check_box(i,j,x):
            # 박스 값에서 지워주고
            base[i//3][j//3].remove(x)
            # 보드에 채워주기
            board[i][j] = x
            if sudoku():
                return True
            # 다시 박스 넣어주고
            base[i//3][j//3].add(x)
            # 값도 초기화
            board[i][j] = 0
    # 안되면 stack에 다시 추가
    stack.append((i,j))
    return False

N = 9
board = [list(map(int, input().split())) for _ in range(N)]
# 3x3 박스 기준으로 set(1,2,...,9)를 만들고 이미 존재하는 값들 지우기
base =[[set([x for x in range(1,10)]) for _ in range(3) ]for _ in range(3) ]
for r in range(3):
    for c in range(3):
        for i in range(3):
            for j in range(3):
                if board[r*3+i][c*3+j]:
                    base[r][c].remove(board[r*3+i][c*3+j])
stack = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            stack.append((i,j))

if sudoku():
    for row in board:
        print(*row)



































# import sys
# from collections import deque
# from pprint import pprint
# import heapq
# input = sys.stdin.readline

# def check_box(i,j,cand):
#     r, c = i//3, j//3
#     if cand in base[r][c]:
#         return True
#     else:
#         return False

# def check_row(i,j, cand):
#     if cand not in board[i]:
#         return True
#     else:
#         return False

# def check_col(i,j,cand):
#     for r in range(9):
#         if i == r:
#             continue
#         if board[r][j] == cand:
#             return False
#     else:
#         return True

# def fill():
#     for row in board:
#         if 0 in row:
#             break
#     else:
#         return True
#     while pq:
#         cost , (i, j) = heapq.heappop(pq)
#         if board[i][j] != 0:
#             continue
        
#         r,c = i//3, j//3
#         cands = base[r][c]
#         for cand in cands:
#             if check_box(i,j,cand) and check_row(i,j,cand) and check_col(i,j,cand) and not board[i][j]:
#                 board[i][j] = cand
#                 base[r][c].remove(cand)
#                 if fill():
#                     return True
#                 board[i][j] = 0
#                 base[r][c].append(cand)

#         break
#     return False

# N = 9
# board = [list(map(int, input().split())) for _ in range(N)]

# pq = []
# base =[[[x for x in range(1,10)] for _ in range(3) ]for _ in range(3) ]
# for r in range(3):
#     for c in range(3):
#         for i in range(3):
#             for j in range(3):
#                 if board[r*3+i][c*3+j]:
#                     base[r][c].remove(board[r*3+i][c*3+j])

# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 0:
#             heapq.heappush(pq, (len(base[i//3][j//3]), (i,j)))
# fill()
# for row in board:
#     print(*row)