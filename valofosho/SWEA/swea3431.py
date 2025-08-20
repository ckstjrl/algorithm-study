T = int(input())
for test_case in range(1, T+1):
    L, U, X = map(int,input().split())
    # 범위 내에 있다는 것을 전제로 ans 초기값 설정
    # else문을 따로 달지 않아도 가능
    ans = 0
    if X > U:
        ans = -1
    elif X < L:
        ans = L-X
    print(f"#{test_case} {ans}")