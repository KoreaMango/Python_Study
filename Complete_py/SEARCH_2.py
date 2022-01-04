import time
start = time.time()  # 시작 시간 저장
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# result = [0  for _ in range(m)]

# for i in range(m):
#     for j in a:
#         if j == b[i]:
#             result[i] = 1

# print(result)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


a.sort()
for i in b:
    result = binary_search(a, i, 0, n-1)
    if result != None:
        print("yes")
    else:
        print("no")


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
