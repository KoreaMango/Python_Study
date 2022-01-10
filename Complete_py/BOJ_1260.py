from collections import deque

def dfs(gragh, v, visited):
    visited[v] = True  # 방문 노드 처리하기
    print(v, end=' ')  # 방문한거 프린트 하기
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True  # 방문 노드 처리하기
    while queue:  # 큐가 빌 때까지
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())  # 입력 받기

arr = [[]]  # 0번 인덱스를 제외하고 선언, 간선이 연결하는 두 정점 번호 받기

for i in range(M):  # 간선의 개수 M
    arr.append(list(map(int, input().split())))  # 리스트 배열 넣기


graph = [[]]  # 0번 인덱스를 제외하고 선언, 인덱스가 정점의 번호이고 간선이 연결된 정점들을 넣는 배열
for i in range(N):  # 정점 개수 만큼 그래프 선언
    graph.append(list())

for i in arr[1:]:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(N+1):
    graph[i].sort()

DFSvisited = [False] * (N + 1)  # 0번 인덱스를 제외했을 때 정점의 개수만큼 선언, 방문 노드 처리
BFSvisited = [False] * (N + 1)


dfs(graph, V, DFSvisited)
print()
bfs(graph, V, BFSvisited)
