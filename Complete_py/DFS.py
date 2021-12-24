def dfs(gragh, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 7],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
