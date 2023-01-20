class operations:
    def transposeMatrix(m):
        return map(list,zip(*m))
    
    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def calc_det(m):
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*calc_det(getMatrixMinor(m,0,c))
        return determinant
    
    def calc_inv(m):
        determinant = calc_det(m)
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
                