'''
4843. 특별한 정렬 (D3)
'''

T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    special = [0 for _ in range(10)]        # 특별히 정렬된 수 10개의 리스트
 
    for i in range(10):                     # 10번 순회
        max_idx, min_idx = i, i
 
        for j in range(i+1, N):             # 정렬되지 않은 인덱스부터 끝까지 중에 최대최소값 뽑기
            if arr[max_idx] < arr[j]:
                max_idx = j
 
            if arr[min_idx] > arr[j]:
                min_idx = j
 
        if i % 2 == 0:                      # 인덱스가 짝수면 최대값을 특별한 정렬에 추가
            special[i] = arr[max_idx]
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:                               # 인덱스가 홀수면 최소값을 특별한 정렬에 추가
            special[i] = arr[min_idx]
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
    print(f'#{tc}', *special)