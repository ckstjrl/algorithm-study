T = int(input())
for test_case in range(1, T+1):
    tc, N = input().split()
    arr = list(input().split())
    ls = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic = {}
    ans = ''
    total = []
    for char in ls:
        # 리스트에 count를 통해 해당 딕셔너리의 키값에 대한 값 설정
        dic[char] = arr.count(char)
        # 딕셔너리의 값을 토대로 문자열을 횟수만큼 반복
        temp = [char] * dic.get(char)
        total.append(' '.join(temp))
    print(tc)
    print(' '.join(total))