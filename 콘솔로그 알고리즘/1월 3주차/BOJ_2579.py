n = int(input())
sta = [0]
for _ in range(n):
    sta.append(int(input()))

# 0이 시작점 1부터 첫번째 계단

dp = [0] * 10001

# 1을 밟은 경우 2, 3 가능           //  
# 2를 밟은 경우                   //  
#   1을 앞에서 밟은 경우 4          //  
#   1을 앞에서 안밟은 경우 3        //     
# 3을 밟은 경우                   //
#   2를 앞에서 밟은 경우 5         //
#   2를 앞에서 안밟은 경우 4        //

dp[1] = sta[1]
if n >= 2:
    dp[2] = sta[1] + sta[2]

for i in range(3, n+1):
    # 현재 계단 + 전전 단계 계단 합,     전전전 계단 합 + 현재계단 + 전계단
    dp[i] = max(dp[i-2] + sta[i], dp[i-3] + sta[i-1] + sta[i])

print(dp[n])
