#boj2903 중앙 이동 알고리즘

order = int(input())

#패턴은 2**order + 1 이 된다

#괄호 안: 한 변에 증가하는 점의 개수를 담당 (2 ** order + 1)
#괄호 밖: 가로 세로로 나타나기 때문에 다시 한 번 제곱
val = (2 ** order + 1) ** 2

print(val)