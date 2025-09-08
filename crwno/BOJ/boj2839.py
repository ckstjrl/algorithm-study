N = int(input())
min_package = 1666
for i in range(N//3 + 1):
    for j in range(N//5 + 1):
        if 3 * i + 5 * j == N:
            if min_package > i + j:
                min_package = i + j

if min_package == 1666:
    print(-1)
else:
    print(min_package)