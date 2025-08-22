# BOJ 2869. 달팽이는 올라가고 싶다 / D2
import sys
A, B, V = map(int, sys.stdin.readline().split())
day = (V-B)//(A-B)
if (V-B)%(A-B) != 0:
    day+= 1

print(day)