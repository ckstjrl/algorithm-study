# BOJ1316 그룹 단어 체커

#단어 수 입력
T = int(input())

count = 0

# 숫자만큼 단어 받기
for tc in range(T):
    
    count += 1

    word = str(input())

    checker = set()

    alphabet = word[0]

    # 연속으로 이어지는 경우에는 규칙을 해치지 않는다
    # 하지만 떨어져서 나타나는 순간 규칙 위반
    # 규칙을 위반하지 않으면 전부 돌기
    for i in range(len(word)):
        if word[i] == alphabet:
            continue
        elif word[i] != alphabet:
            checker.add(alphabet)
            alphabet = word[i]

        # 규칙이 위반이 되면 처음에 추가해줬던 1을 제거 후 루프 탈출
        if word[i] in checker:
            count -= 1
            break

print(count)

