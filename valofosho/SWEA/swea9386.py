T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 0을 기준으로 split하면 빈 문자열 or 1의 연속된 문자열만 담긴다.
    arr = list(input().split('0'))
    ans = len(max(arr))
    print(f"#{test_case} {ans}")