# BOJ21313(D1): 문어
N = int(input())
if N % 2 == 0:
    print('1 2 ' * (N // 2))
else:
    print('1 2 ' * (N // 2), '3', sep='')