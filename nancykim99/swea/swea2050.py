str1 = list(input())

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(str1)): # str1 값 하나마다
    for j in range(len(alphabet)): # alphabet 값과 비교
        if str1[i] == alphabet[j]:
            str1[i] = str(j + 1) # 인덱스 +1 이 원하는 각 알파벳

result = ' '.join(str1) # str으로 만들기
print(result)