import sys
input = sys.stdin.readline

def power(num1, num2, num3):
    if num2 == 1:
        return num1 % num3
    elif num2 % 2 == 0:
        return power(num1, num2//2, num3) ** 2 % num3
    else:
        return power(num1, num2//2, num3) ** 2 * num1 % num3


A, B, C = map(int, input().split())

print(power(A, B, C))