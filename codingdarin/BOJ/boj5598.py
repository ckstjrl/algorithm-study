# BOJ 5598. 카이사르 암호 (D1 / B2)
# https://www.acmicpc.net/problem/5598

# 3문자 역행해 카이사르 암호 해독

word = input()
ans = ''

# 한 글자씩 처리
for c in word:
    # 3글자 이전으로 이동, A보다 작아지면 23칸 +
    if ord(c) - 3 < ord('A'):
        ans += chr(ord(c) + 23)
    else:
        ans += chr(ord(c) - 3)

print(ans)



