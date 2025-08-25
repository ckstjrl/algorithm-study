# input으로 단어를 받아서 list로 저장
word = list(map(str, input()))

# 26자리 알파벳 각 자리에 맞춰서 -1을 시작값으로 맞춰둔 리스트 하나 생성
word_num = ['-1'] * 26

#26자리 알파벳 자리에 맞춰서 딕셔너리 생성
alphabet = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25,
}

for i in range(len(word)):
    if word_num[alphabet[word[i]]] == '-1':
        word_num[alphabet[word[i]]] = str(i)

ans = list(map(int, word_num))

print(*ans)