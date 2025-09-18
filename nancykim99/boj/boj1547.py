'''
(BOJ1547 / D1): 공
'''
N = int(input())
arr = [i for i in range(4)]

arr[1] = '*'

for _ in range(N):
    x, y = map(int, input().split())
    arr[x], arr[y] = arr[y], arr[x]

for i in range(4):
    if arr[i] == '*':
        print(i)