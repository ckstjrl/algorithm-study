"""
문제 정의
1. T = TestCase
2. N = 며칠동안 매매가 열리는지
3. 하루에 살 수 있는 물건의 수는 단 하나다.
4. 최대 이익을 return -> 만약 사지 않는게 유리하다면 0을 return

로직 정의
1. 각 날짜에서 매수 금액에 따라 일자를 순회하며 큰 날짜가 있다면 판다.
2. 만약 각 날짜 보다 이익을 남길 수 없다면 사지도 마라

"""

# Solved
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    max_price = 0
    for i in range(N-1, -1 , -1):
        if max_price < arr[i]:
            max_price = arr[i]
        else:
            total += max_price - arr[i]
    print(f"#{test_case} {total}")

# 1. Test case 7/10 -> Timeout
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     total = 0
#     # 마지막날은 사고 파는게 의미가 없으니 제외
#     for i in range(N-1):
#         interest = 0
#         max_price = max(arr[i+1:N])
#         if arr[i] < max_price:
#             interest += (max_price-arr[i])
#             total += interest
#     print('#'+str(test_case)+' '+str(total))