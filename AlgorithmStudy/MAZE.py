from collections import deque

n, m = map(int, input().split())

myLoc = [1, 1]

arr = []
for i in range(n):
    arr.append(list(map(int, input())))


# 0 은 괴물이 있는 부분
# 1 은 괴물이 없는 부분
# 종점 (n,m)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    return arr[n-1][m-1]


print(bfs(0, 0))

