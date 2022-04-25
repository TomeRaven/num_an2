#Tomer Handali , ID: 206751489

def invert_matrix(A, tol=None):
    import copy


    # Make copies of A & I, AM & IM, to use for row ops
    n = len(A)
    AM = copy.deepcopy(A)
    I = [([0] * len(A)) for i in range(len(A))]
    for i in range(len(A)):
        I[i][i] = 1
    IM = copy.deepcopy(I)

    # Perform row operations
    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(n):  # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:
            #  skip row with fd in it.
            crScaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):

                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    return IM

def neg_mat(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = -A[i][j]
    return A


def mul_mat(A,B):
    rows, cols = len(A), len(B[0])
    result = [([0] * cols) for i in range(rows)]

    # iterate through rows of X
    for i in range(len(A)):
        # iterate through columns of Y
        for j in range(len(B[0])):
            # iterate through rows of Y
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def add_mat(A,B):
    rows, cols = len(A), len(A[0])
    result = [([0] * cols) for i in range(rows)]

    for i in range(len(A)):

        for j in range(len(A[0])):
            result[i][j] = A[i][j]+B[i][j]

    return result



def check_Diag(A):

    for i in range(len(A)):

        sumnum = 0
        for j in range(len(A[0])):
            if i != j:
                sumnum += abs(A[i][j])
        if sumnum > abs(A[i][i]):
            return False

    return True



def start(A,B):


    if not check_Diag(A):
        print('no dominant diagonal\n')

    rows, cols = len(A), len(A)
    L = [([0] * cols) for i in range(rows)]
    U = [([0] * cols) for i in range(rows)]
    D = [([0] * cols) for i in range(rows)]


    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != j and j < i:
                L[i][j] = A[i][j]
            if i == j:
                D[i][j] = A[i][j]
            if i != j and j>i:
                U[i][j] = A[i][j]

    while True:
        print('\n\nEnter 1 for yacovi')
        print('Enter 2 for gaus-zeidel')
        print('Enter 0 to exit')

        choice = int(input())

        if choice == 1:
            yacovi(L,D,U,B)

        elif choice == 2:
            gaus(L, D, U, B)

        elif choice == 0:
            break

        else:
            print('bad input! try again')

def yacovi(L,D,U,B):


    G = mul_mat(neg_mat(invert_matrix(D)),add_mat(L,U))
    H = invert_matrix(D)
    X = [[0]for i in range(len(L))]
    result = [[0]for i in range(len(L))]

    i = 0
    while True:
        print('iteration ', i, ': ', X)
        result = add_mat(mul_mat(G, X),mul_mat(H,B))
        if abs(result[0][0]-X[0][0]) < epsilon or i == 50:
            break

        X = result
        i = i+1


    print("\nTotal iterations: ", i)

    if i == 50:
        print("Result did not converge")





def gaus(L,D,U,B):
    G = mul_mat(neg_mat(invert_matrix(add_mat(L,D))),U)
    H = invert_matrix(add_mat(L,D))
    X = [[0] for i in range(len(L))]
    result = [[0] for i in range(len(L))]
    i=0
    while True:
        print('iteration ', i, ': ', X)
        result = add_mat(mul_mat(G, X), mul_mat(H, B))
        if abs(result[0][0] - X[0][0]) < epsilon or i == 50:
            break
        X = result
        i = i+1

    print("\nTotal iterations: ", i)

    if i == 50:
        print("Result did not converge")


epsilon = 0.00001
#works on any number of variables but not on matrixes that arent N*N

# coefficient matrix:
a = [[4, 2, 0], [2, 10,4],[0,4,5]]

# result matrix:
b = [[2], [6],[5]]


start(a,b)
