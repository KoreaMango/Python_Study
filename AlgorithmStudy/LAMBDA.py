n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(str, input().split())))
    arr[i][1] = int(arr[i][1])

arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')
