from collections import deque

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


def DFS(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if array[x][y] == 0:
        array[x][y] = 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if DFS(i, j) == True:
            result += 1

print(result)
