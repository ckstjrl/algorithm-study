T = int(input())
for test_case in range(1, T+1):
    ans = 0
    str1 = input()
    # 문자열을 뒤집었을 때 같은지 확인
    if str1 == str[::-1]:
        ans = 1
    print(f"#{test_case} {ans}")