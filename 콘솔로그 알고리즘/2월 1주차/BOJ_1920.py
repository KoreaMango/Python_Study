# 딕셔너리를 이용해 문제를 해결함.
# 1. N은 입력받을 숫자의 수
# 2. A는 N개의 배열을 딕셔너리로 저장하는데,
# 	 배열의 숫자가 Key이고, Value를 1로 저장
# 3. M은 찾고 싶은 숫자의 수 (사실 안쓰임)
# 4. list를 입력 받고 for 문을 실행,
#	 i는 list 속 값을 순회함.
# 5. i가 A에 있다면 Value(1)를 출력
#	 i가 A에 없다면 0을 출력


N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()
for i in list(map(int, input().split())):
	print(A.get(i, 0))
