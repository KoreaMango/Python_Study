# 정수 N을 입력 받기
N = int(input())

# DP 테이블 초기화, Index : N의 크기 , 값 : 경우의 수
d = [0] * 1001

# 다이나믹 프로그래밍 진행
# N이 1일때 경우의 수 1개
d[1] = 1

# N이 2일 때 경우의 수 3개
d[2] = 3

# i - 2 전의 경우의 수는 셀 필요가 없음
# 앞에 있는 경우의 수를 다 들고옴
# d[i-1] 은 2 X 1 덮개
# d[i-2] 는 2 X 2 덮개

for i in range(3, N+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[N])