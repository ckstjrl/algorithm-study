'''
백준 문제 1157 : 단어 공부

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''


arr = list(input().lower())   # 입력 문자 다 소문자로 변경
cnt = dict()

for t in arr:     #
    if t in cnt:     # 알파벳이 중복으로 나타날 때마다 cnt 더해주고 싶음
        cnt[t] += 1
    else:
        cnt[t] = 1

a = [ [v, k] for k,v in cnt.items()]
a.sort(reverse=True)
if len(arr) > 1 and a[0][0] == a[1][0]:
    print('?')
else:
    print(a[0][1].upper())