# 1트 - 틀림 A,B,C,D값 중간중간 바꿔놓고 그냥계산함
# A, B, C = map(int, input().split())
# D = int(input())
#
# if D < 60:
#     C += D
# elif 60 <= D < 3600:
#     B += D // 60
#     C += D % 60
# else:
#     A += D // 3600
#     B += (D % 3600) // 60
#     C += D % 60
#
# if C >= 60:
#     C -= 60
#     B += 1
#
# if B >= 60:
#     B -= 60
#     A += 1
#
# if A >= 24:
#     A -= 24
#
# print(A, B, C)

A, B, C = map(int, input().split())
D = int(input())

C += D

if C >= 60:
    nC = C % 60
    nB = B + C // 60
    B = nB
    C = nC
if B >= 60:
    nB = B % 60
    nA = A + B // 60
    A = nA
    B = nB
if A >= 24:
    nA = A % 24
    A = nA
print(A, B, C)