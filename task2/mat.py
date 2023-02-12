class Operations:

    def transposeMatrix(m):
        return list(map(list, zip(*m)))

    def getMatrixMinor(A, i, j):
        return [row[:j] + row[j + 1:] for row in (A[:i] + A[i + 1:])]

    def getMatrixDeternminant(m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * Operations.getMatrixDeternminant(Operations.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(m):
        determinant = Operations.getMatrixDeternminant(m)
        if determinant == 0:
            print(" Please enter a non-singular matrix")
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = Operations.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * Operations.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = Operations.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def getMatrixAdjoint(m):
        if len(m) == 2:
            return [[m[1][1], -1 * m[0][1]],
                    [-1 * m[1][0], m[0][0]]]
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = Operations.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * Operations.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = Operations.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]
        return cofactors

    def display(m):
        for i in range(len(m)):
            for j in range(len(m)):
                print(m[i][j], end=" ")
            print("\n")


if __name__ == "_main_":
    pass        
