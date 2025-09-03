# 3052. 나머지
'''
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성해라.

`set()` : 증복 X, 순서 X
빈 리스트를 만들어서 값 넣은 다음, 중복 제거 후 갯수 뽑자.
'''
a = [int(input()) for _ in range(10)]
lst = []
for i in range(10):
    lst.append(a[i] % 42)
ans = set(lst)
print(len(ans))