# 5598. 카이사르 암호
'''
가이우스 율리우스 카이사르(Gaius Julius Caesar)는 고대 로마 군인이자 정치가였다.
카이사르는 비밀스럽게 편지를 쓸 때, 'A'를 'D로', 'B'를 'E'로, 'C'를 'F'로... 이런 식으로 알파벳 문자를 3개씩 건너뛰어 적었다고 한다.
26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 3문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있다.
이 카이사르 단어를 원래 단어로 돌려놓는 프로그램을 작성하시오.
변환전    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
변환후    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

[입력]
입력은 한 줄로 이루어져 있으며, 그 한 줄에는 대문자 알파벳으로 구성된 단어가 1개 있다. 단어는 최대 1000자 이하이다.

[출력]
입력받은 카이사르 단어를 원래 단어로 고친 걸 출력하시면 된다.

리스트에서 인덱스 값 찾고, - 3 이동
-> % 26을 해서 A 밑으로 가는 건 다시 Z부터 돌 수 있게 하자.
'''
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word = input()
result = []
for char in word:
    idx = 0
    for i in range(26):
        if alpha[i] == char:
            idx = i
            break
    new_idx = (idx - 3) % 26
    result.append(alpha[new_idx])
print(*result, sep='')