layer = int(input())

#매 루프마다 숫자를 1씩 늘려주기 위해서 빈 변수 생성
count = 0

#별이 찍히지 않은 곳은 띄워쓰기가 되기 때문에 저장 공간을 띄워쓰기로 생성
contain = [' '] * layer

for _ in range(layer):
    #매 순회마다 별 개수 하나씩 증가
    count += 1

    #찍어야 하는 별의 개수만큼 띄워쓰기로 찬 저장 공간을 별로 대체하기
    for i in range(count):
        contain[i] = '*'

    #별이 반대로 찍혀야 하기 때문에 reverse로 리스트 순서를 뒤집어주기
    contain.reverse()
    #이미 띄워쓰기를 채워놨기 때문에 합쳐줄때는 띄워쓰기 없이
    ans = ''.join(contain)
    
    print(ans)

    #출력 이후 다시금 저장 공간 초기화
    contain = [' '] * layer
