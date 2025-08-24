# 10809. 알파벳 찾기

T = input()
abc ='abcdefghijklmnopqrstuvwxyz'
for i in abc:
    if i in T:
        print(T.index(i), end=" ")
    else:
        print(-1, end=" ")