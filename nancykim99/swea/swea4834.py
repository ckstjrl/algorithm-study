# T = int(input())

T = 1
N = 10
K = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def selection_sort(a, N) :

	for i in range(N-1) : # 정렬 구간의 시작 인덱스
		min_idx = i # 첫 원소를 최소로 가정
		for j in range(i+1, N) :
			if a[min_idx]> a[j] : # 최소 원소 위치 갱신
				min_idx = j
		a[i], a[min_idx] = a[min_idx], a[i] # 구간 최솟값을 구간 맨 앞으로

for tc in range(1, T+1):
    # N = int(input())
    # arr = list(map(int, input().split()))

    arr = selection_sort(arr,N)

    arr_2 = []

    for i in range(N):
        arr_2.append(arr.pop([0]))
        arr_2.append(arr.pop([-1]))

    print(arr_2)