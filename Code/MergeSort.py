def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p:q+1]
    R = A[q+1:r+1]
    MAX_NUM = float('inf')
    L.append(MAX_NUM)
    R.append(MAX_NUM)

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def main():
    l1 = [3, 5, 7, 43, 243, 543, 234, 76, 276, 2, 5, 15]
    MergeSort(l1, 1, len(l1) - 1)
    print(l1)

if __name__ == '__main__':
    main()
