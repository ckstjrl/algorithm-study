"""
1926. 간단한 369게임
"""

# 사용자로부터 정수 N을 입력받음 (1부터 N까지 숫자를 출력할 예정)
N = int(input())

# 결과를 담을 리스트 생성: 크기 N, 초기값은 공백 문자열 ' '
answer_list = [' '] * N

# 1부터 N까지 숫자를 하나씩 검사
for i in range(1, N + 1):
    # 현재 숫자를 문자열로 변환 (자릿수별로 접근하기 위해)
    char_num = str(i)

    # 각 자리 숫자를 정수로 변환하여 리스트로 저장 (예: 36 -> [3, 6])
    char_num_list = list(map(int, char_num))

    # 3, 6, 9가 몇 번 나오는지 세는 변수
    count_369 = 0

    # 각 자릿수마다 3, 6, 9가 있는지 검사
    for j in range(len(char_num_list)):
        if char_num_list[j] == 3 or char_num_list[j] == 6 or char_num_list[j] == 9:
            count_369 += 1  # 3, 6, 9가 발견될 때마다 카운트 증가

    # 만약 3, 6, 9가 한 번도 안 나왔으면 원래 숫자를 출력 리스트에 저장
    if count_369 == 0:
        answer_list[i - 1] = char_num
    else:
        # 3, 6, 9가 나왔으면 그 횟수만큼 '-' 출력 (예: 2번 나오면 '--')
        answer_list[i - 1] = '-' * count_369

# 리스트에 저장된 결과를 공백으로 구분하여 출력
print(' '.join(answer_list))
