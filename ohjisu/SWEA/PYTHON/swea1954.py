"""
1954. 달팽이 숫자

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

"""
from pprint import pprint

T = int(input()) 
for tc in range(1, T+1) :
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    idx = N
    i = 0
    j = N-1

    arr[0] = [i+1 for i in range(N)]

    def recursive(size, idx, i, j, loop) :
        di = [1, 0, -1, 0] # arr[0]을 주고 시작하기 때문에
        dj = [0, -1, 0, 1] # 방향은 하 좌 상 우 순으로 진행 
        # N-1 * 2번 반복 -> N-2 * 2번 반복 -> ... 1 * 2번 반복
        for _ in range(2) :         # 2번 반복
            for _ in range(size):   # size == (N-1)만큼 반복
                i += di[(loop%4)] 
                j += dj[(loop%4)]
                idx += 1
                arr[i][j] = idx
            loop += 1               # 작은 for문 끝난 후 방향 바꾸기
                
        if idx == N**2 :            # idx가 N*N일 때 끝남
            return 
        recursive(size-1, idx, i, j, loop)  # 안끝난다면 재귀
        
    recursive(N-1, idx, i, j, 0)
    print(f'#{tc}')
    for a in arr : 
        print(*a) 
        


"""
while 문 사용 --> 불필요해서 삭제
"""

# N = int(input())
# arr = [[0] * N for _ in range(N)]
# idx = N
# i = 0
# j = N-1

# arr[0] = [i+1 for i in range(N)]

# # arr = 

# def recursive(size, idx, i, j, loop) :
#     # size가 1일 때까지 도는 while문

#     di = [1, 0, -1, 0] # arr[0]을 주고 시작하기 때문에
#     dj = [0, -1, 0, 1] # 방향은 하 좌 상 우 순으로 진행 
#     # 조건 걸어서 방향 설정 
#     # range_num = 1 if size == 1 else 2
#     for count in range(2) :
#         if size % 2 == 0 :
#             i += di[loop%4] 
#             j += dj[loop%4]  
        
#         idx += 1
        
#         # if count % 2 == 0 and arr[i][j] == 0 :
#         arr[i][j] = idx
        
#         if 
#             return recursive(size-1, idx, i, j, loop+1)

#     # if (size == 0) : # 조건 수정 (arr[i+di[(loop+1)%4]][j+dj[(loop+1)%4]] == 0)
#     #     return recursive(size+1, idx, i, j, loop)
#     if idx == N**2 :
#         return 
    
# recursive(N-1, idx, i, j, 0)
# pprint(arr)

"""
x와 y의 값 조건대로 if문 구성 -- 실패
"""
# def func(N, idx, arr, i, j) :
#     if N == 0  :
#         return arr
    
            
#             x += 1 # di[3]
#             y += 0 # dj[3]
        

    # x == 0, y == 0
    # -> 오른쪽으로
    # if y >= 0 :
    #     x += di[0]
    #     y += dj[0]

    # # x == N-1, y == N-1
    # # -> 왼쪽으로
    # if x == N-1 and y == N-1 : ## N 이 변동값이 아님
    #     x += di[2]
    #     y += dj[2]
    # # x == N-1, y == 0
    # # -> 위로
    # elif x == N-1 and y == 0 : # 딕셔너리 만들어서 up : [x == N-1, y ==o] 형태로 컨디션 담아 놓
    #     x += di[3]
#     #     y += dj[3]
        

#     idx += 1
#     arr[x][y] = idx
#     # N = N-1
#     return func(N, idx, arr, x, y)

# func(N, idx, arr, 0, 2)                  
# print(arr)  

"""
규칙 찾는 중
"""

# x = 0
# y = 0 
# for x in range(N) :
#     if x == 0 :
#         arr[0][0] = x + 1
#         arr[0 + 1][0 + 1 + 1] = x + 1 + 3
#         arr[0 + 1 + 1][0] = x + 1 + 3 + 3
#     if x == 1 :
#         arr[0][1] = x + 1
#         arr[1 + 1][1 + 1] = x + 1 + 3
#         arr[1 + 0][0] = x + 1 + 3 + 3
#     if x == 2 :
#         arr[0][2] = x + 1
#         arr[2][1] = x + 1 + 3
#         arr[1][1] = x + 1 + 3 + 3

#         arr[x][y] = idx+1