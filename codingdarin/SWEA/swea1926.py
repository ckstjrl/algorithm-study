N = int(input())
arr = []  # 1부터 N까지의 요소 N개를 담을 빈 리스트 할당

for i in range(1, N+1):
    arr.append(i) # 리스트에 담기
new_arr = [] # 규칙대로 수정된 요소를 담을 빈 리스트

for i in arr:
    if '3' not in str(i) and '6' not in str(i) and '9' not in str(i):
        #print(i, end=' ')
        new_arr.append(i) # 전체 요소 순회하며 369 규칙 해당하지 않는 요소 담기
    else:
        num = str(i).count('3') + str(i).count('6') + str(i).count('9')
        #print('-'*num, end=' ')
        new_arr.append('-'*num) # 3,6,9 포함 여부 체크될 시, 본 요소 대신에 해당 개수만큼 '-' 추가해 담기

print(*new_arr) #언패킹한 요소 출력