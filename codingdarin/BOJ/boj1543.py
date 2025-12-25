# BOJ 1543. 문서 검색 (D2 /S5)

#---------------------------------2회차 풀이: .count() 메서드 활용

txt = input()
x = input()
print(txt.count(x))

#---------------------------------1회차 풀이: 직접 구현

txt = input()
x = input()
n = len(x)
cnt = i = 0
while i+n <= len(txt):
    if txt[i:i+n] == x:
        cnt += 1
        i +=n
        continue
    i += 1
print(cnt)