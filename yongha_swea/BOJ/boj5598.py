# BOJ5598 카이사르 암호

caesar_num_let = {
    1 : 'A',
    2 : 'B',
    3 : 'C',
    4 : 'D',
    5 : 'E',
    6 : 'F',
    7 : 'G',
    8 : 'H',
    9 : "I",
    10 : "J",
    11 : 'K',
    12 : 'L',
    13 : 'M',
    14 : 'N',
    15 : 'O',
    16 : 'P',
    17 : 'Q',
    18 : 'R',
    19 : 'S',
    20 : 'T',
    21 : 'U',
    22 : 'V',
    23 : 'W',
    24 : 'X',
    25 : 'Y',
    26 : 'Z',
}

caesar_let_num = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26,
}

#혹시 모를 앞뒤 공백 제거하며 단어 받기
word = input().strip()

#변환 과정을 받아줄 빈 리스트 생성
word_to_num = []

num_to_word = []

#단어를 떼어서 알파벳에서 숫자로 1차 변환
for i in word:
    word_to_num.append(caesar_let_num[i] - 3)

#숫자를 알파벳으로 2차 변환 이 과정에서 0과 같거나 작아지는 경우 다시 숫자 26을 추가
for i in range(len(word_to_num)):
    while word_to_num[i] <= 0:
        word_to_num[i] += 26

# 이후 변환 된 철자를 하나씩 받아서 다시 하나의 단어로 완성
for i in word_to_num:
    num_to_word.append(caesar_num_let[i])

# 띄워쓰기를 제거하며 다시 하나의 단어로 만들어 저장
caesar_word = ''.join(num_to_word)

#단어 출력
print(caesar_word)


