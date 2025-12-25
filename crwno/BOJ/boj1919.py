word_1 = input()
word_2 = input()

check = [0] * 26

for i in word_1:
    check[ord(i) - 97] += 1

cnt = 0

for j in word_2:
    if check[ord(j) - 97] != 0:
        check[ord(j) - 97] -= 1
        cnt += 1

ans = len(word_1) + len(word_2) - cnt * 2
print(ans)