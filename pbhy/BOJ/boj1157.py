# 1157. 단어 공부
'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
대문자와 소문자를 구분하지 않는다.

입력된 단어를 딕셔너리에서 알파벳은 key, 나온 숫자 갯수를 value로 만듦
value의 최대 갯수를 구해서 key만 모은 리스트 생성
위 리스트의 길이가 1개면 그 key 출력, 2개 이상이면 '?' 출력
'''
word = input().upper()  # 문자열 입력을 대문자로 변환
cnt = dict()  # 문자를 저장할 빈 딕셔너리 생성
for t in word:   # t : cnt의 key
    if t in cnt:
        cnt[t] += 1 # t가 cnt에 있으면 밸류값 +1
    else:
        cnt[t] = 1
max_cnt = max(cnt.values()) # max 밸류값 구하기
result = [k for k, v in cnt.items() if v == max_cnt]    # 밸류값이 최대인 key 리스트로 모음
if len(result) == 1:
    print(result[0])
else:   # 밸류값 최대인  key 리스트가 2개 이상이면
    print('?')