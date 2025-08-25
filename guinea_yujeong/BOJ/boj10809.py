# 10809번 알파벳 찾기

S = input()
abc ='abcdefghijklmnopqrstuvwxyz'  #전체 알파벳 입력

for i in abc: 
    if i in S:  # abc변수를 반복문을 이용하여 알파벳 존재 유무 확인
        print(S.index(i), end= ' ')  #end= ' ' <- 가로 출력
    else:
        print( -1, end =' ')  #존재하지 않는 알파벳 -1로 반환 후 출력 