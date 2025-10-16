S = input()

def check(s):  # 회문이면 True반환
    if s == s[::-1]:
        return True
    else:
        return False

for i in range(len(S)):  # 맨 앞글자 하나씩 없애고 회문인지 검사
    if check(S[i:]):  # 남은 부분이 회문이면 지금까지 제거한 부분 거꾸로 뒤집어서 붙이기
        add = S[:i][::-1]
        ans = S + add
        print(len(ans))
        break