import numpy as np
def Eigen(Matrix):
    e, V = np.linalg.eig(Matrix)
    print("Matrix:\n %s" % V)
    print("Eigenvector: %s" % e)

def Survival(J, A, R, Adult, Child):
    years = 10
    Temp = Adult
    for i in range(years):
        Adult = Adult*A
        Adult += Child*J
        Child = Temp/R
        Temp = Adult
    print("Adults: %s" % Adult)
    print("Child: %s" % Child)



A = np.matrix('1 2 ; 3 2')
Eigen(A)
A = np.matrix('2 -4 ; -1 -1')
Eigen(A)
A = np.matrix('7 0 -4 ; 0 5 0 ; 5 0 -2')
Eigen(A)
A = np.matrix('1 1 -3 ; 2 0 6 ; 1 -1 5')
Eigen(A)
A = np.matrix('0 1 0 ; 3 0 1 ; 2 0 0')
Eigen(A)
A = np.matrix('3 1 1 ; -4 -2 -5 ; 2 2 5')
Eigen(A)
A = np.matrix('2 1 1 ; 0 1 0 ; 1 -1 2')
Eigen(A)


Adults = 100
Child = 40
Rate = 2
SurvA = 1/2
SurvC = 1/2
Survival(SurvC, SurvA, Rate, Adults, Child)
Rate = 3
SurvA = 1/4
SurvC = 1/4
Survival(SurvC, SurvA, Rate, Adults, Child)
Rate = 2
SurvA = 1/4
SurvC = 1/3
Survival(SurvC, SurvA, Rate, Adults, Child)
Rate = 3
SurvA = 3/5
SurvC = 5
Survival(SurvC, SurvA, Rate, Adults, Child)
print("Question 4:")
Rate = 2
SurvA = 1/2
SurvC = 1/6
Survival(SurvC, SurvA, Rate, Adults, Child)
print("Question 5:")
Rate = 2
SurvA = 1/2
SurvC = 2/5
Survival(SurvC, SurvA, Rate, Adults, Child)


