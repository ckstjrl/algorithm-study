# 4837. 부분집합의 합 D2
# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = 12

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    sum_list = []
    a = 0
    for i in range(1 << 12):  # arr의 부분집합
        subset = []
        subset_sum = 0

        for j in range(12):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # 1의 j번 비트가 1인경우
                subset.append(arr[j])
                subset_sum += arr[j]

        if len(subset) == N and subset_sum == K:
            cnt += 1


    print(f'#{tc}', cnt)





# 해결방법 : 비트연산으로 부분집합을 생성하는 방법
# arr = [13,6,7,1,5,4]
# n = len(arr) # n : 원소의 개수
# for i in range(1<<n) : # 1<<n : 부분 집합의 개수
# 	for j in range(n): # 원소의 수만큼 비트를 비교함
# 		if i & (1<<j): # 1의 j번 비트가 1인경우
# 			print(arr[j], end=", ") # j번 원소 출력
# 	print()
# print()
# 시행착오 1 : sum을 구하지 않고 찾아보려고 함