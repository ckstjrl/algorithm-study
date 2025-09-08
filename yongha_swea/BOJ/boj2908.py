#input으로 들어오는 두 개의 값을 변수 두개에 각각 할당
A, B = map(str, input().split())

#두 개의 input 값을 리스트로 받아올 빈 리스트 생성
list_A = []
list_B = []

#각 값을 하나씩 list에 item으로 넣어주기
for i in A:
    list_A.append(i)

for j in B:
    list_B.append(j)    

#값의 순서를 반대로 뒤집기
list_A.reverse()

list_B.reverse()

#반대로 뒤집힌 값들을 기반으로 대소 비교 후 join하여 출력
if list_A > list_B:
    reverse_A = ''.join(list_A)
    print(reverse_A)
else:
    reverse_B = ''.join(list_B)
    print(reverse_B)