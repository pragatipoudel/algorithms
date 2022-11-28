

def binary_addition(A,B,n):
    key = 0;
    carry = 0;
    C = [0]*(n+1)
    for i in range(n-1, -1, -1):
        key = A[i] + B[i] + carry
        if key == 2:
            key = 0;
            carry = 1
        elif key == 3:
            key = 1
            carry = 1
        else:
            carry = 0
        C[i+1] = key
    C[0] = carry
    return C

A = [0, 1, 1, 1]
B = [0, 0, 1, 0]
n = len(A)

d = binary_addition(A,B,n)
print(d)