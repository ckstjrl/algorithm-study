T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    if str1 in str2:
        cnt = 1
    print(f"#{test_case} {cnt}")