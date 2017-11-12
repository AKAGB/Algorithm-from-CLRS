# 4.1 FIND_MAX_SUBARRAY
"""
利用分治法，将最长子序列问题分解为3部分
[low...mid]、[mid..high]、[i...mid...j]中找到最长子序列
"""

def find_max_crossing_subarray(A, low, mid, high):
    """
    param:  A -> list
            low -> 列表最小下标
            mid -> 列表中间元素下标
            high -> 列表最大下标
    return: [i...mid...j] 的(i, j, sum)
    """
    left_sum = float('-inf')
    total = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        total = total + A[i]
        if total > left_sum:
            left_sum, max_left = total, i

    right_sum = float('-inf')
    total = 0
    max_right = 0
    for i in range(mid+1, high+1):
        total = total + A[i]
        if total > right_sum:
            right_sum, max_right = total, i

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    """
    param:  A -> 列表
            low -> 最小下标
            high -> 最大下标
    return: 最大子序列的(最小下标，最大下标，和)
    """

    if high == low:
        return (low, high, A[low])
    mid = (high + low) // 2
    left_low, left_high, left_sum = \
        find_maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = \
        find_maximum_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = \
        find_max_crossing_subarray(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    if right_sum >= cross_sum and right_sum >= left_sum:
        return (right_low, right_high, right_sum)
    return (cross_low, cross_high, cross_sum)

def main():
    # 最大子序列是[18, 20, -7, 12]
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, high, total = find_maximum_subarray(A, 0, len(A)-1)
    print('Result = ' + str(A[low:high+1]))

if __name__ == '__main__':
    main()
