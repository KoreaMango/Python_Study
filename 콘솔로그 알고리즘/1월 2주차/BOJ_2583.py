import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())

arr = [[False] * N for _ in range(M)]

for i in range(K):
    loc = list(map(int, input().split()))
    leftBottomX = loc[0]
    leftBottomY = M - loc[1] - 1
    rightTopX = loc[2] - 1
    rightTopY = M - loc[3]
    arr[leftBottomY][leftBottomX] = True
    arr[rightTopY][rightTopX] = True

    for j in range(rightTopY, leftBottomY + 1):
        for i in range(leftBottomX, rightTopX + 1):
            arr[j][i] = True

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
result = [0 for _ in range(K+1)]


def dfs(arr, x, y):
    result[cnt] += 1
    flag = True
    if arr[y][x] == False:
        arr[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M:
                if arr[ny][nx] == False:
                    dfs(arr, nx, ny)


for i in range(M):
    for j in range(N):
        if arr[i][j] == False:
            cnt += 1
            dfs(arr, j, i)

print(cnt)
result = sorted(result)
for i in range(K+1):
    if result[i] != 0:
        print(result[i], end=' ')
