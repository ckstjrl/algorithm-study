"""
1954. 달팽이 숫자

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

"""

"""
기본 -> x 순회
for x in range(N)
if x == N-1 :
    for y in range(N)
        ..
       

"""
"""
인덱스: 0 ~ N까지 --
넣을 값: 1, N+1
"""

# N = int(input())
N = 3
arr = [[0] * N for _ in range(N)]
idx = 3
x = 2
y = 0

arr[0] = [i+1 for i in range(N)]


if x == N-1 :
    for y_1 in range(1, N) :
        idx += 1
        arr[y_1][x] = idx
        if y_1 == N-1 :
            for x_1 in range(N-2, -1, -1) :
                idx += 1
                arr[y_1][x_1] = idx
                if x_1 == 0 :
                    for x_2 in range(0, N-1) :
                        idx += 1
                        arr[y_1-1][x_1] = idx
                    break
                    
                
            
        
    

    print(arr)  


# for y in range(0, N) :
#     for x in range(0, N) :
#         idx += 1
#         arr[y][x] = idx
#         if x == N-1 :
#             for y_1 in range(1, N) :
                
#                 idx += 1
#                 arr[y_1][x] = idx
#                 if y_1 == N-1 :
#                     for x_1 in range(N-2, -1, -1) :
#                         idx += 1
#                         arr[y_1][x_1] = idx
#                         if x_1 == 0 :
#                             for y_2 in range(2, N-1) :
#                                 idx += 1
#                                 arr[y_2][x_1] = idx
#                                 if y_2 == N-1 :

                                
#                                     print(arr)

# arr[0] = [i+1 for i in range(N)]

# def loops_x(y, idx, start, stop) :
#     for x in range(start, stop) :
#         idx += 1
#         arr[x][y] = idx
#     return arr

# def loops_y(x, idx, start, stop) :
#     for y in range(start, stop) :
#         idx += 1
#         arr[x][y] = idx
#     return arr

# # for y in range(N) :
# #     for x in range(N) :
# #         idx += 1
# #         arr[y][x] = idx 
# x = N-1
# y = 0
# if x == N-1 :
#     arr = loops_y(x, idx, 1, N-1)
# if y == N-1 :
#     arr = loops_x(y, idx, N-1, -1)
# print(arr)





# def loops(arr, N) :
#     global idx
#     idx += 1
#     arr[x][y] = idx
#     if x == N-1 :
#         return loops(arr[1:], x)
#     if y == N-1 :
#         return loops(arr[1:], y)
#     return  arr

# idx = 0
# arr[0] = [i+1 for i in range(N)]

# def loops(arr, start, stop, step) :
#     global idx
#     for item in range(start,  stop, step) :
#         idx += 1
#         arr[x][y] = idx
#         if x == stop-1 :
#             loops(arr, )

# loops(arr[0], 0, )


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