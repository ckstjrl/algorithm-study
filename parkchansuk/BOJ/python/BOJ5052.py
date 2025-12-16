# BOJ 5052. 전화번호 목록 / D3
'''
전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.

전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26
이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다.
전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다.
따라서, 이 목록은 일관성이 없는 목록이다.
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    pn = []
    for _ in range(N):
        pn.append(sys.stdin.readline().strip())

    pn.sort() # 기본 정렬을 진행하면 알아서 짧은 번호가 앞으로 오게됨
    ans = 'YES'
    for i in range(N-1):
        if pn[i+1].startswith(pn[i]):
            ans = 'NO'
            break
            
    print(ans)
'''
짧은 번호가 긴 번호 맨 앞에 포함 되는 경우가 있는지 없는지 확인해야함.
반복문을 사용하기 위해서 짧은 번호가 앞쪽에 오게 만들어야 함...
    for i in range(N-1):
        for j in range(1, N-i):
            if pn[i] == pn[i+j][:len(pn[i])]:
                ans = 'NO'
이런 식의 이중 for문을 써도 답은 나오지만 시간 초과 발생하므로 
startswith 함수 활용
str.startswith(str_) 의 경우 str 앞부분에 str_이 있는지 없는지 확인함.
'''