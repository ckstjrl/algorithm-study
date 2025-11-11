'''
BOJ2447 / D3): 별 찍기 - 10

해결 방법 : 
1. 문자열로 만들고 뽑기 -> 줄바꿈이 제대로 안 됨
2. 리스트로 만들고, 재귀해서 예쁘게 뽑으려고 했음 -> 리스트 안에 리스트 안에 리스트...로 예쁘게 안 뽑힘...
    1) 가장 작은거 만들고
    2) 그 작은걸로 똑같이 채우고
    3) 2번으로 똑같이 채우기
3. 분할정복으로 풀기. 27에서 3 나누면서 가장 작은 1까지 내려감. 1부터 패턴 만들기

메모 : 
`N**(1/3)` : 제곱근 하는 법
* 분할 정복 다시 해보니까 너무 헷갈려요...ㅠㅠ
* 별 찍기 싫어요. 그냥 손으로 찍어!
'''
N = int(input())

n = int(N**(1/3))

def draw_recur(n):
    if n == 1:
        return ['*']
    pre_pattern = draw_recur(n // 3) # 작은 패턴들을 재귀적으로 호출해서 얻기 (분할정복)
    new_pattern = []
    for i in range(3):
        for line in pre_pattern:
            if i == 1: # 가운뎃 줄이라면
                new_pattern.append(line + ' ' * (n // 3) + line) # 중간에 빈 공간 만들기
                # 빈 공간 -> n // 3인 만큼 공간 만들기
            else:
                new_pattern.append(line * 3)
    return new_pattern

ans = draw_recur(N)

print('\n'.join(ans))