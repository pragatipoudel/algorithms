def binary_search(arr, a, b, number):
    if b>=a:
        mid = (a+b) // 2
        if number == arr[mid]:
            return mid
        elif number < arr[mid]:
            return binary_search(arr,a,mid-1,number)
        else:
            return binary_search(arr,mid+1,b,number)
    else:
        return -1

arr = [2,3,4,10,40]
x = int(input("enter a number:"))

result = binary_search(arr,0,len(arr)-1,x)
if result != -1:
    print(result)
else:
    print("Element not present") 