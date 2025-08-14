"""
Counter 함수를 호출해서 사용하는 방법은 제외
"""
# from collections import Counter
# T = int(input())
# for test_case in range(1,T+1):
#     str1 = Counter(list(input()))
#     most = str1.most_common(1)
#     answer = list(input()).count(most)
#     print(f"#{test_case} {answer}")

T = int(input())
for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    dic = dict()
    for i in range(len(str2)):
        # 딕셔너리에 값이 없다면 0으로 디폴트 값 채우기
        dic.setdefault(str2[i],0)
        # 밸류 값을 + 1
        dic[str2[i]] += 1
    set_a = set(str1)
    max_c = 0
    # 가장 많이 나온 횟수를 찾기
    for i in set_a:
        c = dic.get(i)
        if c > max_c:
            max_c = c
    print(f"#{test_case} {max_c}")