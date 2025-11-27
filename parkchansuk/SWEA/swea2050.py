# 2050. 알파벳을 숫자로 변환 /D1
dict = {}
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(1, 27):
    dict[alpha[i-1]] = str(i)
    # dict에 알파벳을 키로 숫자를 벨류로 넣음

T = list(input())
arr = [] # 벨류를 추가할 빈 리스트 생성
for j in T:
    arr.append(dict[j])

print(' '.join(arr))