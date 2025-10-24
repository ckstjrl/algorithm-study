# boj9093 단어 뒤집기

T = int(input())

for tc in range(T):
    #후입선출 방식으로 출력, 트리거는 띄워쓰기를 기준으로 stack의 값을 전부 하나씩 출력하여 정답에 추가한다
    stack = []

    answer = ''

    arr = input()

    for i in arr:
        if i != ' ':
            stack.append(i)

        else:
            while stack:
                answer = answer + stack.pop()
            answer += ' '

    # 마지막으로 stack에 띄워쓰기와 남은 마지막 단어 정답에 추가해주기
    while stack:
        answer = answer + stack.pop()

    print(answer)