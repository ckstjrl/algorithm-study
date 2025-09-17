"""
[문제]
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

[출력]
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""
## 시간 초과 남 
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def recursive(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        y = recursive(x, n/2)
        return y * y
    else:
        y = recursive(x, (n-1)/2) 
        return y * y * x

ans = recursive(A, B)
print(ans % C)


## 내장함수 쓰기
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
print(pow(A, B, C))


## 분할 정복 - 시간초과 없이
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod_pow(a, b, m):
    if b == 0:
        return 1 % m
    # 절반 문제로 쪼개기 (정수 나눗셈 필수)
    t = mod_pow(a, b // 2, m)
    t = (t * t) % m          # 매 단계 모듈러로 수를 작게 유지
    if b % 2 == 1:
        t = (t * (a % m)) % m
    return t

print(mod_pow(A % C, B, C))