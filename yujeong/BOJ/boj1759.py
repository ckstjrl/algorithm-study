# 1759. 암호 만들기

# 암호는 L개로 구성, 주어지는 문자는 C개
L, C = map(int, input().split())
chars = list(input().split())
chars.sort()    # 알파벳이 증가하는 순서로 암호를 만들기 위해 문자 리스트 정렬

vowels = ['a', 'e', 'i', 'o', 'u']  # 알파벳 모음 리스트

# 문자열이 모음 개수 >=1, 자음 개수 >=2 만족하는지 
def check_cnt(code):
    v_cnt = c_cnt = 0                       # 모음 개수, 자음 개수 카운트
    for c in code:
        if c in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    return (v_cnt >= 1) and (c_cnt >= 2)    # 모음과 자음 개수가 조건에 맞는지 반환

# 백트래킹으로 문자 리스트에서 암호 만들고 조건에 맞으면 출력
def backtracking(code):
    if len(code) == L:                      # 만들어진 암호 길이가 L이면
        if check_cnt(code):                 # 모음, 자음 개수가 조건에 맞으면
            print(code)                     # 출력
        return

    for x in range(len(code), C):           # 문자 리스트의 문자 중
        if code[-1] < chars[x]:             # 증가하는 순서로 올 수 있는 문자면
            code += chars[x]        
            backtracking(code)              # 그 문자를 더해서 탐색 이어감
            code = code[:-1]                # 백트래킹


for i in range(C - L + 1):  # 알파벳이 증가하는 순서로 암호를 만들어야 하므로, 최대 인덱스 범위는 C-L
    backtracking(chars[i])