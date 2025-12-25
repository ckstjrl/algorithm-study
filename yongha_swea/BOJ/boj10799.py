#BOJ10799 쇠막대기

sticks = input()

stick_stack = []

count = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        stick_stack.append('(')
    else:
        # 레이저 발싸 ('()') - stack에 들어간 갯수 = 막대기 높이, 전체 다 절단되기 때문에 그 수 만큼 카운트 추가
        if sticks[i-1] == '(':
            stick_stack.pop()
            count += len(stick_stack)
        # 막대 끝이라는 뜻, 막대 한 조각을 count에 더해주기
        else:
            stick_stack.pop()
            count += 1

#전체 조각수 출력
print(count)