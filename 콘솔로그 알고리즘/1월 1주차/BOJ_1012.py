
from collections import deque
import sys
sys.setrecursionlimit(100000)
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(graph, y, x):
    graph[y][x] = 2  # 방문 노드 처리하기

    for k in range(4):
       nx = x + dx[k]  # 다음 위치 이동 x좌표
       ny = y + dy[k]  # 다음 위치 이동 y좌표
       if nx >= 0 and ny >= 0 and nx < M and ny < N:  # 배열 밖으로 안나가게 처리
           if graph[ny][nx] == 1:  # 다음 좌표의 위치가 1이면
               dfs(graph, ny, nx)  # 그 위치에서 다시 dfs 실행


T = int(input())  # 테스트 케이스 수
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())  # 가로길이, 세로길이, 배추가 심어져 위치의 개수

    graph = [[0] * M for _ in range(N)]  # 배열 생성 및 초기화

    for i in range(K):
        tmp = list(map(int, input().split()))  # 입력 받은 위치에 1로 설정
        graph[tmp[1]][tmp[0]] = 1  # 세로 위치, 가로 위치

    for i in range(N):  # 배열 세로만큼 반복
        for j in range(M):  # 배열 가로 만큼 반복
            if graph[i][j] == 1:  # 1인 위치를 만나면 dfs 실행
                dfs(graph, i, j)
                cnt += 1  # 카운트 증가
    print(cnt)
