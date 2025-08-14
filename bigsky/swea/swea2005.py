# 조합을 통해 파스칼의 삼각형 만들기
# 0C0 / 1C0, 1C1 / 2C0, 2C1, 2C2 / ...
import math
 
def combination(n: int, k: int):
    if n >= k:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#'+str(tc))
    for i in range(N):
        for j in range(N):
            if i >= j:
                print(combination(i, j), end=' ')
        print()


# solved 1. 파스칼 삼각형을 이차원 배열을 통해 만들기
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     pascal_list = []
 
#     for i in range(N):
#         row = [1] * (i + 1)
#         if i > 1:
#             for j in range(1, i):
#                 row[j] = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
#         pascal_list.append(row)
 
#     print('#'+str(tc))
#     for row in pascal_list:
#         print(*row)