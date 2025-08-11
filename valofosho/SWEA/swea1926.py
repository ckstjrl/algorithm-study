# 1번 풀이 str.replace 활용
N = int(input())
arr = [str(i) for i in range(1,N+1)]
for char in arr:
    # 문자열에 3, 6, 9가 들어있으면 '-'로 치환
    temp = char.replace('3','-').replace('6','-').replace('9','-')
    # 변환된 적이 있으면 카운트별로 출력
    if temp.count('-') > 0:
        print(f"{'-'*temp.count('-')}", end = ' ')
    else:
        print(char, end = ' ')

# 2번 풀이 filter 조건을 풀기
N = int(input())
arr = [str(i) for i in range(1, N+1)]
# 3, 6, 9 가 들어있는지 확인을 위한 필터 설정
filter = ['3', '6', '9']
for i in range(N):
    filtered = 0
    # 문자열 내 각 글자에 대해 필터에 걸리면 +1
    for char in arr[i]:
        if char in filter:
            filtered += 1
    # 필터링 된 횟수만큼 '-' 연속 출력
    if filtered:
        arr[i] = '-'*filtered
print(' '.join(arr))