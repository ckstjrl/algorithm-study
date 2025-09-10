# 2941. 크로아티아 알파벳
'''크로아티아 알파벳	변경
č : c=
ć : c-
dž : dz=
đ : d-
lj : lj
nj : nj
š : s=
ž : z=
ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
위 목록에 없는 알파벳은 한 글자씩 센다.

인덱스를 끊어서 보자.
- dz= : [i:i+3]로 3개를 봐서 있으면 갯수 +1
-> 이 경우 그 다음 i는 +3
- 나머지 크로아티아 알파벳은 [i:i+2]로 2개를 봐서 있으면 갯수 +1
-> 이 경우 그 다음 i는 +2
- 일반 알파벳은 그냥 갯수 +1 & 그 다음 i는 +1
'''
word = input()
cro_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
i = 0
count = 0
while i < len(word):
    if word[i:i+3] in cro_alpha:    # 3글자 : dz=
        count += 1
        i += 3
    elif word[i:i+2] in cro_alpha:  # 2글자 검사
        count += 1
        i += 2
    else:       # 일반 알파벳 : 1글자
        count += 1
        i += 1
print(count)