def maxCrossingSubArray(arr, l, m, h):
    left_sum = None
    sum = 0

    for i in range(m, l-1, -1):
        sum = sum + arr[i]
        if (left_sum is None or sum > left_sum):
            left_sum = sum

    right_sum = None
    sum = 0

    for i in range(m+1, h+1):
        sum = sum + arr[i]
        if (right_sum is None or sum > right_sum):
            right_sum = sum
        
    highest_array = max(left_sum, right_sum, left_sum + right_sum)
    return highest_array

def maxSubArraySum(arr, l, h):
    if (l > h):
        return -10000
    if (l==h):
        return arr[l]
    m = (l + h) // 2
    highest = max(maxSubArraySum(arr, l, m - 1), maxSubArraySum(arr, m + 1, h), maxCrossingSubArray(arr, l, m, h))
    return highest

arr = [-2, -3, 2, 3, -2, 10, -4]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is", max_sum)

