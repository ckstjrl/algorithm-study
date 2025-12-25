# BOJ12605 단어순서 뒤집기

T = int(input())

for tc in range(T):

    # 리스트에 단어들 담아주기
    arr = list(map(str, input().split()))

    # 단어 하나마다 기준으로 뒤집기
    reverse_arr = list(reversed(arr))

    # 리스트에 있는 뒤집힌 값들을 그 사이사이 스페이스를 추가하며 합해주기
    answer = ' '.join(reverse_arr)

    # tc는 loop 순서 +1
    print(f'Case #{tc+1}: {answer}')