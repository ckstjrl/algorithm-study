'''
백준 2547번 : 사탕 선생 고창영

각 테스트 케이스에 대해 모두에게 같은 사탕을 나눠줄 수 있으면 YES를, 없으면 NO를 출력한다.
'''

T = int(input())

for _ in range(T):
    input()
    N = int(input())    # 학생 수 입력받기
    s = 0               # 사탕
    for i in range(N):  # 학생 수 만큼 반복 각 학생의 사탕 개수 읽고 합치기
        s += int(input()) # 정수로 변환하고 s에 더하기
    print("YES" if s % N == 0 else "NO")  # s % N == 0 -> 공평하게 분배 가능

'''
memo 
신기한 input()
if문과 else문을 가로로 입력함
'''