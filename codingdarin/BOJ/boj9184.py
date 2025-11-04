# BOJ 9184. 신나는 함수 실행 (D2 / S2)
# ----------------------------2회차 풀이: 데코레이터 활용
from functools import lru_cache

@lru_cache(maxsize=None)
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break    
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")


# # ----------------------------1회차 풀이: 메모이제이션
# def w(a, b, c):
#     # 메모값 있으면 바로 리턴
#     if (a,b,c) in memo:
#         return memo[(a,b,c)]
    
#     if a <= 0 or b <= 0 or c <= 0:
#         result = 1

#     elif a > 20 or b > 20 or c > 20:
#         result = w(20, 20, 20)

#     elif a < b and b < c:
#         result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     else:
#         result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
#     # 메모값 저장
#     memo[(a,b,c)] = result
    
#     return result

# # 여러 테케에서의 재사용을 위해 전역에서 메모장 초기화    
# memo = {}

# while True:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         break    
#     print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

