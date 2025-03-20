# Solve System of equations with gaussian elimination algorithm
# Your name:  

import numpy as np

# exchange rows i and j in matrix M
def swap(M, i, j):
        if i==j:
                return
        else:
                Trow = M[i,].copy()
                M[i,]=M[j,]
                M[j,]=Trow

# multiply row i by the number a
def mult(M, i, a):
        M[i,]=a*M[i,]

# multiple row i by number a and add to row j and replace row j
#  a*r(i) + r(j) -> r(j)
def er3(M, i, a, j):
        M[j,]=a*M[i,]+M[j,]

def findNZEntry(M, top):
        # find non zero entry starting at row top, search column by column.
        mrows, mcols = M.shape
        for icol in range(mcols):
                for irow in range(top,mrows):
                        if (M[irow,icol]!=0 ):
                                return (irow, icol)
        return (-1,-1) # matrix is all zeros

def rref(M):
    # input - matrix m augmented matrix for system of equations
    # return - matrix m in reduced row echelon form
    mrows, mcols = M.shape
    for top in range(mrows):
            arow, acol = findNZEntry(M, top)
            if arow==-1:
                    return M
            else:
                    swap(M, top, arow)
                    mult(M, top, 1.0/M[top,acol]) # make the leading entry a 1
                    # make everything below leading 1 a zero
                    for irow in range(top+1,mrows):
                            er3(M, top, -M[irow,acol], irow)
                    # make everything above the leading 1 a zero
                    for irow in range(top):
                            er3(M, top, -M[irow,acol], irow)     
    return M
        

def rank(M):
    # input - matrix m is augmented matrix in reduced row echeclon format
    # return - rank of matrix m
    #       if M is inconsistent, then return 0
    #       M is inconcsistent if there is a row that has a leading 1 in the
    #         last column
    nrows, ncols  = M.shape
    rank = -1
    #   YOUR CODE GOES HERE
    rank += 1
    if np.linalg.matrix_rank(M) != np.linalg.matrix_rank(M[:,:-1]):
        return 0
    for row in range(nrows):
        if np.any(M[row, :-1] == 1):
            rank += 1
    return rank
           

print("Test 1- 2 variables, 2 equations, 1 solution.")
M = np.matrix('3. 4. 5.; 1. 2. 3.')
# save a copy of M
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
# answer is in last column of M
# verify answer by doing R[coefficients] X M[last column] == R[constants]
print("verify answer")
print (np.matmul(R[:,0:mcols-1], M[:,mcols-1]))
print("expected answer")
print(R[:,mcols-1])


print("Test 2 - 3 variables, 3 equations, one solution.")
M = np.matrix([[1., 1., 1., 5.],[1., -1., 2., 11.],[1., -1., -2., -5.]])
# save a copy of M
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
# answer is in last column of M
# verify answer by doing R[coefficients] X M[last column] == R[constants]
print("verify answer")
print (np.matmul(R[:,0:mcols-1], M[:,mcols-1]))
print("expected answer")
print(R[:,mcols-1])


print("Test 3 - 6 variables, 3 equations, multiple solutions.")
M = np.matrix('0. -1. 3. 1. 3. 2. 1.; 0. -2. 6. 1. -5. 0. -1.; 0. 3. -9. 2. 4. 1. -1.; 0. 1. -3. -1. 3. 0. 1.')
# save a copy of M
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
print('the rank is less than number of variables', mcols-1, ' so there are many solutions.')


print("Test 4 - 3 variables, 3 equations, inconsistent. No solution.")
M = np.matrix([[1., 1., 1., 5.],[1., -1., 2., 11.],[2.0, 0.0, 3.0, 15.0]])
# save a copy of M
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
print('the rank is 0, so the equations are inconsistent.')


print("Personal Test 5 - 3 variables, 3 equations, 1 solution.")
M = np.matrix([[1., 1., 2., 8.],[3., -1., 1., 0.],[-1., 3., 4., -4.]])
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
print('the rank is equal to the number of variables, so the equations have 1 solution.')




print("Personal Test 6 - 3 variables, 3 equations, Many Solutions.")
M = np.matrix([[-2., 3., 3., -9.],[3., -4., 1., 5.],[-5., 7., 2., -14.]])
R = M.copy()
mrows, mcols = M.shape
print(M)
M = rref(M)
print("Row echelon form")
print(M)
r = rank(M)
print('rank =', r)
print('the rank is less than number of variables', mcols-1, ' so there are many solutions.')
