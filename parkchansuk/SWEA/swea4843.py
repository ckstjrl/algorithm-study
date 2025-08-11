# 특별한 정렬 / D3
def find_max_idx(a, n): # 최대값의 인덱스 추출
    max_v = 0
    for i in range(n):
        if max_v < a[i]:
            max_v = a[i]
            max_idx = i
    return max_idx

def find_min_idx(a, n): # 최솟값의 인덱스 추출
    min_v = 100
    for i in range(n):
        if min_v > a[i]:
            min_v = a[i]
            min_idx = i
    return min_idx

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    special_list = [] # 특별한 정렬
    for k in range(N, 0, -2): # 최대 최소를 pop하기 때문에 2개 간격으로 뽑음
        a = find_max_idx(arr, k) # 최댓값의 인덱스를 a로 설정
        special_list.append(arr.pop(a)) # 최댓값 pop하여 특별 정렬에 넣기
        b = find_min_idx(arr, k-1) # 최댓값을 pop해서 원소 개수 -1
        special_list.append(arr.pop(b)) # 최솟값을 pop하여 특별 정렬에 넣기

    special_list_10 = []  # 10개 원소만 넣기
    for e in range(10):
        special_list_10.append(special_list[e])

    print(f'#{tc} {" ".join(map(str, special_list_10))}')