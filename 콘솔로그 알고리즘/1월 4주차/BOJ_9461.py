import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0 for _ in range(N+1)]
    if N == 1 or N == 2 or N == 3:
        print("1")
        continue
    dp[1] = 1
    dp[2] = 1
    for i in range(3,N+1):
        dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[N])