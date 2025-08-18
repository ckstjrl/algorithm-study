T = int(input())
for test_case in range(1, 1+T):
    word = input()
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0
    print(f'#{test_case} {ans}')