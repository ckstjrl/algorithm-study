C = int(input())
for tc in range(1, 1 + C):
    N, *arr = map(int, input().split())

    average = sum(arr) / N
    count = 0
    for i in arr:
        if i > average:
            count += 1
    print(f"{count / N * 100:.3f}%")