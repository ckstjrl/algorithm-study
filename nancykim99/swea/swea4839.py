# 4839. 이진탐색 D2
# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
# A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
# 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1 <= Pa, Pb < P <=1000
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

T = int(input())

for tc in range(1, T+1):
	P, Pa, Pb = map(int, input().split())

	def binarysearch(N, key):  # key를 찾으면 인덱스, 실패하면 -1 반환
		start = 1 # 페이지 번호는 1부터 시작하기 때문
		end = N
		search_num = 1
		while start <= end:
			middle = (start + end) // 2
			search_num += 1 # middle을 새로 구할때마다 +1
			if middle == key:  # 검색 성공
				return search_num
			elif middle > key:  # 찾는 값보다 크면
				end = middle  # 왼쪽 구간 선택
			else:  # 찾는 값보다 작으면
				start = middle  # 오른쪽 구간 선택
		return

	A_search = binarysearch(P, Pa)
	B_search = binarysearch(P, Pb)

	# A와 B 횟수 비교
	if A_search > B_search:
		result = 'B'
	elif B_search > A_search:
		result = 'A'
	elif A_search == B_search:
		result = '0'

	print(f'#{tc}', result)


# 해결 방법 : 이진탐색
# 시행착오 1 : while문이 돌때마다 search_num이 추가가 되지 않았음 -> middle을 찾아버리면 중간에 break가 되기 때문
# 	그래서 +1하는 부분을 while문 바로 밑으로 옮김 -> while문 돌아갈때마다 추가 가능
# 시행착오 2 : return middle을 계속 넣어놔서 return 값이 middle이었음. 그래서 break로 바꾸고 return이 search_num이 되도록 함
# 시행착오 3 : 페이지에서 찾는거기 때문에 end가 N-1이 아니라 N이어야 함
# 시행착오 4 : search_num = 1 -> 무조건 한 번은 서치를 함
# 시행착오 5 : 중복을 포함하고 있음 -> middle -1, +1이 아닌 그냥 middle로 함

