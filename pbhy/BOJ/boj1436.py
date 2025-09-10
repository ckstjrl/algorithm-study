# 1436. 영화감독 숌
'''
N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오.

문자열에서 '666'이 들어가는 것 찾아내자.
'''
n = int(input())
cnt = 0
ans = 666
while True:
    if '666' in str(ans):
        cnt += 1
    if cnt == n:
        break
    ans += 1
print(ans)