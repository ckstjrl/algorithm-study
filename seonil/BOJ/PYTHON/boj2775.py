"""
2775. 부녀회장이 될테야

 ex1) 1층 3호에는 몇명이 살까?
 0층 1호 + 0층 2호 + 0층 3호 = 1 + 2 + 3 = 6
 ex2) 2층 3호에는 몇명이 살까?
 1층 1호 + 1층 2호 + 1층 3호 = 1 + (1+2) + (1+2+3) = 10
 ex3) 3층 3호에는 몇명이 살까?
 2층 1호 + 2층 2호 + 2층 3호 = 1 + (1+(1+2)) + (1+(1+2)+(1+2+3)) = 15

 * 내가 찾은 규칙:
 1. k층 1호에는 반드시 1명이 산다!
 2. k층 n호에 사는 사람 수
 = (k-1)층 1호 + (k-1)층 2호 + ... + (k-1)층 (n-1)호 + (k-1)층 n호
 = k층 (n-1)호 + (k-1)층 n호

 ** 처음에 그냥 재귀함수로 풀었더니 시간초과되길래 어떻게 연산량을 줄이지 고민하다가,
 수업 시간에 배운 memoization이 떠올라서 적용했더니 풀렸다.

 """

def get_residents(k, n, memo={}):

    if (k, n) in memo:  # 이미 memo 딕셔너리에 k층 n호의 거주민 수를 계산한 값이 있으면 그대로 반환
        return memo[(k, n)]

    if k == 0:  # 0층일 때: n호에는 n명이 산다 (기초 조건)
        return n
    if n == 1:  # 1호에는 항상 1명만 산다
        return 1

    # 점화식: k층 n호 = k층 (n-1)호 + (k-1)층 n호
    # memo 딕셔너리에 k층 n호의 거주민 수를 저장하여 중복 계산을 방지(memoization)
    memo[(k, n)] = get_residents(k, n - 1, memo) + get_residents(k - 1, n, memo)

    # k층 n호의 거주민 수 반환
    return memo[(k, n)]


T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):
    k = int(input())  # 층 수 입력
    n = int(input())  # 호 수 입력

    # k층 n호의 거주민 수 출력
    print(get_residents(k, n))



# 시간 초과 : 일반 재귀함수로 구현한 version
# def get_residents(k, n):
#
#     if k == 0:
#         return n
#     if n == 1:
#         return 1
#     else:
#         return get_residents(k, n-1) + get_residents(k-1, n)