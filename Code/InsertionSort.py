def InsertionSort(a):
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
    InsertionSort(numbers)
    print('Sorted list:', str(numbers))

if __name__ == '__main__':
    main()
