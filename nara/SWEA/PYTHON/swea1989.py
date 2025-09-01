def is_palindrome(txt):
    for i in range(len(txt)//2):
        if txt[i] != txt[len(txt)-i-1]:
            return False
    return True
T = int(input())
for test_case in range(1, T + 1):
    txt = list(map(str, input()))
    if is_palindrome(txt) == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')