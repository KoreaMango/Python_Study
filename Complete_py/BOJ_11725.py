import sys
sys.setrecursionlimit(10**9)

N = int(input())  # 노드의 개수
arr = [[] for _ in range(N+1)]  # 인덱스가 정점의 번호

for i in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

parent = [0 for _ in range(N+1)]


def func(arr, v, dif):
    for i in arr[v]:
        if i != dif:
            parent[i] = v
            func(arr, i, v)


func(arr, 1, 0)

for i in parent[2:]:
    print(i)
