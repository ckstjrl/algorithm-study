T = int(input())

for tc in range(1, T+1):
    str1, str2 = map(str, input().split())

    cnt = str1.count(str2)

    without_str2 = str1.replace(str2,'')

    cnt += len(without_str2)

    print(f'#{tc} {cnt}')