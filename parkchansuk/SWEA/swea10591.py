# 이진탐색 / D2
def binary_select(a, n, key): # 이진함수
    l = 0
    r = n-1
    cnt = 0
    while l <= r :
        cnt += 1 # 탐색 횟수 계산
        c = int((l + r) / 2)
        if a[c] == key:
            break
        elif a[c] > key: # 원래는 r=c-1로 설정해야 하지만 문제에서 r=c로 설정
            r = c
        elif a[c] < key: # 원래는 l=c+1로 설정해야 하지만 문제에서 l=c로 설정
            l = c
    return cnt # 탐색 횟수를 출력해줌

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = []
    for page in range(1, P+1):
        arr.append(page)

    A_cnt = binary_select(arr, P, A) # A가 걸린 횟수
    B_cnt = binary_select(arr, P, B) # B가 걸린 횟수

    if A_cnt < B_cnt :
        win = 'A'
    elif A_cnt > B_cnt :
        win = 'B'
    else:
        win = '0'

    print(f'#{tc} {win}')