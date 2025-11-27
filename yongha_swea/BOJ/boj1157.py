#boj1157: 단어 공부

#전부 대문자로 변환하여서 받기
word = input().upper()

#set으로 변환하는 과정을 통해서 중복 제거
word_list = list(set(word))

#각 글자가 나온 횟수를 셀 빈 리스트 생성
word_count = []

#각 글자가 나온 횟수를 세서 카운트 리스트에 추가
for i in word_list:
    letter_count = word.count(i)
    word_count.append(letter_count)

#두 개 이상의 글자가 동일한 횟수가 나올 경우 ? 출력
if word_count.count(max(word_count)) > 1:
    print('?')

#하나인 경우에는 해당 글자 출력
else:
    print(word_list[(word_count.index(max(word_count)))])