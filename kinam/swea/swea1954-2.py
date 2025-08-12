'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

from pprint import pprint

N = 6
arr = [[0] * N for _ in range(N)]

#내가 찾은 달팽이 규칙 N / (N-1) (N-1) / (N-2) (N-2) / ... / 1 1
#                    우    하    좌       상    우    하좌  


di = [0, 1, 0, -1] #델타 이용해서 재귀함수 내부의 방향전환 쉽게 해볼 것
dj = [1, 0, -1, 0] #우 하 좌 상 순으로 


def loops(arr, i, j, N, num, dir):
    ''' 1. 숫자를 채워넣는다
    2. 방향을 바꾼다
    3. 종료조건까지 반복'''

    if num > N*N: #재귀종료
        return #뭐반환하지..........반환할게 없음 


    arr[i][j] = num #지금 위치에 숫자 채우기

    ni = i + di[dir]
    nj = j + dj[dir] 

    new_dir = dir
    #방향 바꿀 조건?
    #다음 인덱스가 이미 채워져있거나 >> 0이 아님
    #다음 인덱스가 없거나? (N을 넘어가거나?) >> ni nj의 인덱스 조건 
    if not ((0 <= ni < N) & (0 <= nj < N)) or arr[ni][nj] != 0:
        #방향 바꿈..........
        #di dj의 다음 인덱스로 가야함
        #단순히 +=1 하면 인덱스 벗어남
        # %4 하고 나머지에 +1 하면 안벗어날듯
        #new_dir = dir % 4 + 1 // dir == 3 일때가 문제 생김
        new_dir = (dir + 1) % 4

        #ni, nj 그대로 loops에 넘겨주면 안되니까 수치 조정
        ni = i + di[new_dir]
        nj = j + dj[new_dir] # 바뀐 new_dir로 재할당


    loops(arr, ni, nj, N, num+1, new_dir)

loops(arr, 0, 0, N, 1, 0)

pprint(arr)