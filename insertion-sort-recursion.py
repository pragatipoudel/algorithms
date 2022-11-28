def insertion_sort(arr,n):
    if n == 1:
        return
    insertion_sort(arr,n-1)
    key = arr[n-1]
    i = n-2
    while (i > -1) and (arr[i] > key):
        arr[i+1] = arr[i]
        i = i - 1
    arr[i+1] = key

arr = [5, 15, 35, 8, 6, -6, 3.2]
n = len(arr)
insertion_sort(arr,n)
print(arr)