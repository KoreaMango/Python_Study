import copy

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for i in range(n):
    tmp = input()
    for j in range(m):
        graph[i][j] = tmp[j]

# ----------------- 배열 입력 받는 코드
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
flag = ['W', 'B']
# 8 X 8 보드의 왼쪽 위 첫번째 칸이 움직이면 보드 값이 다 바뀌므로
# 첫번째 칸을 보드의 인덱스로 쓰면 됨

tmp = m * n
for i in range(n-7):  # 세로 인덱스
    for j in range(m-7):  # 가로 인덱스
        for p in range(2):
            arr = copy.deepcopy(graph)
            cnt = 0
            if arr[i][j] != flag[p]:
                arr[i][j] = flag[p]
                cnt += 1
            for a in range(8):  # 자른 보드 탐색
                for b in range(8):
                    for k in range(4):
                        nx = j + b + dx[k]
                        ny = i + a + dy[k]
                        if nx < j+8 and ny < i+8 and nx >= j and ny >= i:
                            if arr[i+a][j+b] == arr[ny][nx]:
                                cnt += 1
                                if arr[ny][nx] == 'B':
                                    arr[ny][nx] = 'W'
                                else:
                                    arr[ny][nx] = 'B'

            res = min(cnt, tmp)

            tmp = res

print(res)
