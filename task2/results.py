from matrix_operations import Operations

if __name__== "__main__" :
    n_s = input(" Enter the dimension of matrix A: ")
    n = int(n_s)
    A = [[float(input(f" Enter a element of row {(i+1)} & column {(j+1)} : ")) for j in range(n)] for i in range(n)]
    B = [[float(input(f" Enter a element of row {(i+1)} & column {(j+1)} : ")) for j in range(n)] for i in range(n)]
    
    print("Input matrix A is :")
    Operations.display((A))

    print("\nThe determinent for a is :")
    print(Operations.getMatrixDeternminant(A))

    print("\nThe Adjoint for a is :")
    Operations.display(Operations.getMatrixAdjoint(A))

    print("\nThe Inverse for a is  :")
    Operations.display(Operations.getMatrixInverse(A))

    print("Input matrix B is :")
    Operations.display((B))

    print("\nThe determinent for b is :")
    print(Operations.getMatrixDeternminant(B))

    print("\nThe Adjoint for b is :")
    Operations.display(Operations.getMatrixAdjoint(B))

    print("\nThe Inverse for b is :")
    Operations.display(Operations.getMatrixInverse(B))
    C = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] * B[i][j]
