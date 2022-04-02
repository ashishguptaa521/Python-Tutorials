def solve(A, B):
    A = []
    B = []
    z = 0
    for i in range(len(A)) and j in range(len(B)):
        z = max([(A[i] + B[j]), (A[j] + B[i])])
    return z


a = [1,2]
b = [2, 3]
print(solve(a, b))
