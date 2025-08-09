# 간단한 369게임 / D2
N = int(input())
arr = [str(i) for i in range(1, N+1)]

for j in range(N): # j는 인덱스 값
    cnt = 0 # 3, 6, 9 개수를 세기 위한 counter
    for k in range(len(arr[j])): # k는 arr[j]에 있는 str을 받아 3, 6, 9 몇개를 포함하는지 확인 (어떤 숫자여도 상관없게 하기 위해)
        if '3' in arr[j][k]:
            cnt += 1
        if '6' in arr[j][k]:
            cnt += 1
        if '9' in arr[j][k]:
            cnt+= 1
    
    if cnt >= 1: # 3, 6, 9 포함되어 있으면 arr[j]를 -*cnt로 변경
        arr[j] = '-'*cnt
        
print(' '.join(arr))