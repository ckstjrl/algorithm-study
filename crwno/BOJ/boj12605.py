N = int(input())
for tc in range(1, N + 1):
    arr = list(map(str, input().split()))
    print(f'Case #{tc}:', end=' ')
    for i in range(len(arr) - 1):
        print(arr[-i - 1], end=' ')
    print(arr[0])