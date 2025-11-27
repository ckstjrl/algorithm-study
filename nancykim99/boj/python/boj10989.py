# 10689. 수 정렬하기 3 D1
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# [입력]
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# [출력]
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 처음에 푼 방법 -> 메모리 초과
# N = int(input())
#
# arr = [0]
# for _ in range(N):
#     num = int(input())
#     arr.append(num)
#
# arr.sort()
#
# for i in range(N):
#     print(arr[i])

# 시행착오 1 : 10000보다 작거나 같은 숫자기에 10001로 했어야 함

N = int(input())

arr = [0] * 10001

for _ in range(N):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)







