'''
(BOJ10707 / D1): 수도요금
'''

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

x = A * P

if P <= C:
    y = B
else:
    y = B + ((P - C) * D)

print(min(x, y))