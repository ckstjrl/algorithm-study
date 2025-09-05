T = int(input())

for tc in range(T):
    code = ''
    
    # 반복횟수, 문자열 받기
    repeat, arr = input().split()

    # repeat의 횟수만큼 문자열의 각 글자를 변수에 추가
    for i in arr:
        code += (i * int(repeat))

    print(code)