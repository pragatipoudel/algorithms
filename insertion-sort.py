

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i > -1) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

B = [34, 52, 45, 9, 89, 94]
insertion_sort(B)
print(B)
