N = int(input())
if N % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            print(1, end=' ')
        else:
            print(2, end=' ')
else:
    for i in range(N - 1):
        if i % 2 == 0:
            print(1, end=' ')
        else:
            print(2, end=' ')
    print(3)