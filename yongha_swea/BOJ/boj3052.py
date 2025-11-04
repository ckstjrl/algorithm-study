T = 10

empty_list = []

#42의 나머지를 list에 하나씩 추가
for tc in range(T):
    num = int(input())
    rest = num % 42
    empty_list.append(rest)

#set을 이용해서 중복 제거
remover = set(empty_list)

#set내부에 아이템 길이를 세서 출력
print(len(remover))
    