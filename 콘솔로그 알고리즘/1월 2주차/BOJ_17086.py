# 초기화 코드
N, M = map(int, input().split())

arr = []  # 아기 상어 배열
for i in range(N):
    arr.append(list(map(int, input().split())))

# 구현 코드

dx = [1, -1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
cnt = 1  # 거리 카운트 변수
while min(map(min, arr)) == 0:  # bfs
    for i in range(N):
        for j in range(M):  # 배열 크기 만큼 탐색
            if arr[i][j] == cnt:  # 상어가 1이므로 1을 찾으면 방문
                for k in range(8):  # 주위를 방문하기 시작한다.
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if nx >= 0 and ny >= 0 and nx < M and ny < N:  # 인덱스를 넘지않는 범위에서
                        if arr[ny][nx] == 0:  # 방문을 안한곳을 찾아요
                            arr[ny][nx] = cnt + 1

    cnt += 1  # 반복 카운트 증가


print(max(map(max, arr)) - 1)
