# 1254. 팰린드롬

S = input()
l = len(S)

for i in range(l):              # 문자열을 앞에서부터 차례로 보면서
    if S[i:] == S[i:][::-1]:    # 여기서부터 끝까지 봤을때 팰린드롬이면
        print(len(S) + i)       # 지금까지 본 글자수 (인덱스) + S 길이가 가장 짧은 팰린드롬
        break