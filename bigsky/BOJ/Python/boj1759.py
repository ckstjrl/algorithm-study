# BOJ1759(D3): 암호 만들기
from itertools import combinations

L, C = map(int, input().split())
chars = input().split()

# 모음과 자음 나누기
vowel = []
consonant = []
for char in chars:
    if char in 'aeiou':
        vowel.append(char)
    else:
        consonant.append(char)

# 모음 수 + 자음 수 == L이 될 때,
# 해당 개수만큼 조합으로 빼서 정렬하고,
# 문자열로 anss에 append
anss = []
for i in range(1, len(vowel)+1):
    for j in range(2, len(consonant)+1):
        if i + j != L:
            continue
        pw_vowels = list(combinations(vowel, i))
        pw_consonants = list(combinations(consonant, j))
        for pw_vowel in pw_vowels:
            for pw_consonant in pw_consonants:
                pw = sorted(pw_vowel + pw_consonant)
                anss.append(''.join(pw))
anss.sort()

for ans in anss:
    print(ans)