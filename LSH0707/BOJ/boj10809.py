a = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = []
for i in alpha:
    b = a.find(i)  # 주어진 단어에 알파벳 리스트 순서대로 find() 사용해 인덱스 반환 (없으면 -1)
    ans.append(b)
print(*ans)