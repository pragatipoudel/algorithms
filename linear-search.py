A = [34, 52, 45, 9, 89, 94]
v = input('Enter a number:')
v = int(v)


flag = 0;
for i in range(len(A)):
    if A[i] == v:
        print(i)
        flag = 1
        break
if flag == 0:
    print("Nil")
