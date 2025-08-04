"""
1859. 백만 장자 프로젝트

다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
-> N일 동안 가장 작은 매매가를 기록하는 구매보다 판매 수익이 더 클 때 판다!
--> 1일 : 1로 1개 구매 -> 2일: 2로 1개 구매 -> 3일 :2개를 팖
내 잔액은 0으로 설정
내 물건은 0으로 설정

3일 동안의 판매가가 가장 낮은 지점을 찾음
3일 동안의 판매가가 가장 높은 지점이 첫 인덱스일 경우 -> 0 반환
-- 아닐 경우
나보다 낮은 값 찾기
1.1. 나보다 낮으면 -> 판다
1.2. 나보다 크면 -> 판매가 재설정

arr를 순회하면서 내 다음 값과 비교하면서 wallet과 inventory에 item과 idx를 채워 넣기
나보다 큰 값이 나오면 바로 팔기
나보다 작은 값이 나오면 다시 wallet과 inventory 채워넣기


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
각 날의 매매가는 10,000이하이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.

[예제 풀이]
1번째 케이스는 아무 것도 사지 않는 것이 최대 이익이다.
2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익을 얻을 수 있다.
"""




"""
4트
오답 ... 

"""

# T = int(input())
T = 1
for test_case in range(1, T + 1):
    # N = int(input())
    N = 5
    # arr = list(map(int, input().split()))
    arr = [10, 2, 2, 2, 10]

    if (arr[0] == max(arr)) and  (arr.count(max(arr)) == 1):
        wallet = 0
    else :
        wallet = 0
        # price 초기값을 맨 마지막 값으로 설정
        price = arr[-1]
        # 뒤에서부터 순회
        for idx in range(N-1, -1, -1) :
            # 맨 뒤의 값이 바로 전 값보다 크거나 같을 경우
            if arr[idx] >= arr[idx-1] :
                # wallet에 (시가 - (idx-1 시점의 구매가))를 더하기
                wallet += (price-arr[idx-1])
            # 만약 클 경우
            elif arr[idx] < arr[idx-1]   :
                # 판매가 재설정
                price = arr[idx-1]

    print(f'#{test_case} {wallet}')


"""
3트

오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 10개의 테스트케이스 중 2개가 맞았습니다.
"""

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     if arr[0] == max(arr) :
#         wallet = 0
#     else :
#         wallet = 0
#         price = arr[-1]
#         for idx in range(len(arr)-1, 0, -1) :
#             if arr[idx] >= arr[idx-1] :
#                 wallet += (price-arr[idx-1])
#                 # inventory += 1
#             elif arr[idx] < arr[idx-1]   :
#                 price = arr[idx-1]

#     print(f'#{test_case} {wallet}')


"""
2트

제한시간 초과가 발생하였습니다. 제한시간 초과로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
"""

# import Math

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     if arr[0] == max(arr) :
#         wallet = 0
#     else :
#         wallet = 0
#         inventory = 0
#         for idx in range(len(arr)) :
#             if idx != len(arr)-1 and (arr[idx] <= arr[idx+1]) and Math.mean(arr[idx:])!= min(arr) : ## 여기!! 저 너무 어려워요.... 
#                     wallet -= arr[idx]
#                     inventory += 1
#             elif arr[idx] > arr[idx-1]   :
#                 wallet += arr[idx] * inventory
#                 inventory = 0

#     print(f'#{test_case} {wallet}')


"""
1트

채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 10개의 테스트케이스 중 2개가 맞았습니다.
"""


# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     if arr[0] == max(arr) :
#         wallet = 0
#     else :
#         wallet = 0
#         inventory = 0
#         for idx in range(len(arr)) :
#             if idx != len(arr)-1 and arr[idx] <= arr[idx+1] :
#                 wallet -= arr[idx]
#                 inventory += 1
#             else :
#                 wallet += arr[idx] * inventory
#                 inventory = 0

#     print(f'#{test_case} {wallet}')