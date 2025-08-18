'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우,
 str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.

3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''
T = int(input())
for t in range(1, T+1):

    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    #중복 제거 세트
    set1 = set(str1)
    set2 = set(str2)
    cross = set1 & set2 # 교집합세트

    no_str1 = list(set1)
    no_str2 = list(set2)
    no_cross = list(cross)

    max_list = []
    for i in no_cross: # 문자열 str1과 str2 둘다 포함된 교집합 리스트 순회
        cnt = 0 # 교집합 문자를 세기 위한 카운트 변수
        for j in str2: # str2 순회
            if i == j: # 교집합 문자가 str2에 있으면
                cnt += 1
        max_list.append(cnt) # 글자의 갯수 추가

    max_num = max(max_list) # 가장 많은 글자의 수
    max_str = no_cross[max_list.index(max_num)] # 가장 많은 글자

    print(f"#{t} {max_num}")