def merge(A, p, q, r):
    i = p
    j = q + 1
    k = p
    tmp = [0 for i in range(r+1)]

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[k] = A[i]
            k += 1
            i += 1

        else :
            tmp[k] = A[j]
            j += 1
            k += 1
        
    while i <= q :
        tmp[k] = A[i]
        k += 1
        i += 1

    while j <= r :
        tmp[k] = A[j]
        j += 1
        k += 1

    for a in range(p,r+1):
        A[a] = tmp[a]


def mergeSort(A, p, r):
    if p < r:
        q = int((p + r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


def init(C, D):
    return C+D


def goodResult(A,p,r):
    print("합친 배열 \t\t", A)
    mergeSort(A, p, r)
    print("정상적인 출력 \t ", A)
    print()


def badResult(A,p,r):
    print("합친 배열 \t\t", A)
    mergeSort(A, p, r)
    print("finished mergesort : ", A)
    print()


def main():
    C = list(map(int, input().split()))
    print("C : \t" , C)
    D = list(map(int, input().split()))
    print("D : \t", D)
    print()

    A = init(C, D)
    badResult(A,11,2)

main()
