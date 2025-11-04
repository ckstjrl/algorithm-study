import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    a, b, c = map(int, input().split())
    print(min(a, b, c))  # a mod b = b mod c = c mod a (a=b=c)인 경우에만 가능