T = int(input())

for t in range(T):
    n_sum = 0
    nums = list(map(int, input().split()))
    for n in nums:
        n_sum += n 
    
    n_avg = round(n_sum / 10)
    
    print(f'#{t+1} {n_avg}')