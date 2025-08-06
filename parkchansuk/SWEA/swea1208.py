# Flatten / D3
T = 10
for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(1, dump+1):
        max_v = max(arr)
        min_v = min(arr)
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))
        if max_v - min_v >= 2:
            arr[max_idx] -= 1
            arr[min_idx] += 1

        else:
            break
    
    max_v = max(arr)  # 최종 덤프를 한 후 max값, min 값이 최신화 되어야 함
    min_v = min(arr)    
    
    print(f'#{tc} {max_v - min_v}')