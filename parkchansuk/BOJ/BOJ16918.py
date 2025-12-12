# BOJ 16918. 봄버맨 / D2
'''
문제
봄버맨은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.

폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다. 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다. 봄버맨은 다음과 같이 행동한다.

1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
4. 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
5. 3과 4를 반복한다.
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.

예를 들어, 초기 상태가 아래와 같은 경우를 보자.

...
.O.
...
1초가 지난 후에는 아무 일도 벌어지지 않기 때문에, 위와 같다고 볼 수 있다. 1초가 더 흐른 후에 격자판의 상태는 아래와 같아진다.

OOO
OOO
OOO
1초가 지난 후엔 가운데에 있는 폭탄이 폭발해 가운데 칸과 인접한 네 칸이 빈 칸이 된다.

O.O
...
O.O
입력
첫째 줄에 R, C, N (1 ≤ R, C, N ≤ 200)이 주어진다. 둘째 줄부터 R개의 줄에 격자판의 초기 상태가 주어진다. 빈 칸은 '.'로, 폭탄은 'O'로 주어진다.

출력
총 R개의 줄에 N초가 지난 후의 격자판 상태를 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

# 폭탄 좌표를 배열로 반환하는 함수
def find_bomb(arr):
    bomb_axis = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bomb_axis.append((i, j))
    return bomb_axis

# 폭발 후 배열 반환하는 함수
def explode(arr):
    # 초기값
    nxt = [['O'] * C for _ in range(R)]
    # parameter를 통해 폭탄의 위치 좌표 받음
    q = deque(find_bomb(arr))
    
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # BFS 활용히여 폭발 표현
    while q:
        i, j = q.popleft()
        nxt[i][j] = '.'
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                nxt[ni][nj] = '.'
    return nxt

# N초 상태를 나타내는 배열 반환
def print_now(n):
    # 1초는 항상 초기 상태 반환
    if n == 1:
        return arr

    # 2의 배수인 경우 모든 칸에 폭탄 존재
    if n % 2 == 0:
        return arr1
    # 2의 배수가 아닌 경우
    else:
        # 3, 7, 11 등 4로 나누었을 때 나머지가 3일 때는 초기상태 폭탄이 터지는 경우와 동일
        if n % 4 == 3:
            return arr2
        # 5, 9, 13 등 4로 나누었을 때 나머지가 1일 때는 3, 7, 11에서 남은 폭탄 기반으로 터짐
        else:
            return arr3

R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
arr1 = [["O"]*C for _ in range(R)]
arr2 = explode(arr)
arr3 = explode(arr2)

now_arr = print_now(N)
for i in range(R):
    print(''.join(now_arr[i]))
    
'''
4초 주기로 똑같은 배열이 반환되는 것을 확인
총 4개의 배열 필요
1. 초기상태
2. 폭탄으로 가득찬 배열
3. 초기상태에서 터진 배열
4. 3번 상태에서 터진 배열

폭발 상태는 explode 함수를 통해 구함
BFS 활용
'''