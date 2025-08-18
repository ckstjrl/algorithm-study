# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for test_case in range(1, T+1):

    # 회문 여부를 검사할 단어 입력
    word = input()

    # 회문 여부를 저장할 변수 (기본값: True)
    check_palindrome = True

    # 문자열의 양쪽 끝에서부터 비교
    for i in range(len(word)):
        # 앞에서 i번째 문자와 뒤에서 i번째 문자가 다르면 회문이 아님
        if word[i] != word[len(word) - 1 - i]:
            check_palindrome = False  # 회문 아님
            break  # 더 이상 비교할 필요 없으니 반복 종료

    # 결과 출력 (회문이면 1, 아니면 0)
    print(f'#{test_case} {1 if check_palindrome else 0}')
