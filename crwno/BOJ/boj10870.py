def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x - 1) + f(x - 2)
N = int(input())
print(f(N))