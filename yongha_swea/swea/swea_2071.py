T = int(input())
 
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
 
    count = 0
    num_sum = 0
 
    for i in arr:
        count += 1
        num_sum = num_sum + i
 
    ans = num_sum / count
 
    print(f'#{tc} {round(ans)}')

