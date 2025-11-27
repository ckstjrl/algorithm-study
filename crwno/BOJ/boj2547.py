# blank박아도 되나
T = int(input())

for tc in range(1, T + 1):
    blank = input()
    N = int(input())
    candy = [int(input()) for _ in range(N)]

    sum = 0
    for i in range(N):
        sum += candy[i]

    if sum % N == 0:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)