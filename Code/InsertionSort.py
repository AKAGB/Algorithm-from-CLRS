def Sort(a):
    """
    传入参数为列表，返回有序列表(升序)
    时间复杂度为O(n^2)
    """

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i >= 0 and a[i] > key):
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key

def main():
    num = int(input('Please input the length of array:'))
    print('Enter the numbers:')
    numbers = []
    for each in range(num):
        numbers.append(int(input()))
    Sort(numbers)
    print('Sorted list:', str(numbers))

if __name__ == '__main__':
    main()
