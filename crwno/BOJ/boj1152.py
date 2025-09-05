# 1트 단어 0개 일 때 생각 안함
# s = input().strip()
# res = 1
# for i in range(len(s)):
#     if s[i] == ' ':
#         res += 1
#
# print(res)

s = input().strip()
res = 0
for i in range(len(s)):
    if s[i] == ' ':
        res += 1
if len(s) == 0:
    ans = 0
else:
    ans = res + 1
print(ans)