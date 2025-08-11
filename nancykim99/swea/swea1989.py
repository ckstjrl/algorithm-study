T = int(input())

for tc in range(1, T+1):
    str1 = str(input())

    r_str1 = str1[::-1]
    if str1 == r_str1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')