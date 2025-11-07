'''
BOJ1629. 곱셈

해결방법 : 분할정복을 활용한 거듭제곱
그냥 거듭제곱으로 하면 시간초과 뜬다

def iterative_power(C, n):
    result = 1
    for i in range(1, n):
        result = result * C
    return result

print(iterative_power(A, B) % C)
'''
import sys
A, B, C = map(int, sys.stdin.readline().split())

def recursive_power(C, n, divider):
    if n == 1:
        return C % divider
    if n % 2 == 0: # if n is even
        y = recursive_power(C, n / 2, divider)
        return (y * y) % divider
    else: # if n is odd
        y = recursive_power(C, (n - 1) / 2, divider)
        return (y * y * C) % divider

print(recursive_power(A, B, C))


