import numpy as np

def obereDreiecksMatrix(A,b):
    # überprüfen dass Matrix quadratisch ist:
    if (len(A) != len(A[0])):
        return
    
    n = len(A)
    numberOfRowSwaps = 0

    for i in range(len(A[0])): 

        # Nullen auf Diagonale eliminieren

        if ((A[i,i] == 0)):
            rowToSwapWith = -1
            for j in range(i + 1, n):
                if ((A[j,i] != 0) and (rowToSwapWith == -1)):
                    rowToSwapWith = j
            if(rowToSwapWith == -1):
                print("invalid")
                return
            
            copyA = np.copy(A)
            A[i] = copyA[rowToSwapWith]
            A[rowToSwapWith] = copyA[i]

            copyb = np.copy(b)
            b[i] = copyb[rowToSwapWith]
            b[rowToSwapWith] = copyb[i]

            numberOfRowSwaps += 1

        # Eliminationsschritt

        for j in range(i + 1, n):
            b[j] = b[j] - A[j,i]/A[i,i] * b[i] 
            A[j] = A[j] - A[j,i]/A[i,i] * A[i]

    A_triangle = A

    # Determinante berechnen

    detA = -1 ** numberOfRowSwaps
    for i in range(n):
        detA *= A[i,i]
    
    # auflösen nach x

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i] -= A[i,j] * x[j]

        x[i] = b[i] / A[i,i]

    return [A_triangle, detA, x]


# Wird nur ausgeführt wenn explizit dieses Script ausgeführt wird. 
if __name__ == "__main__":

    A = np.array([[1, 5, 6], [7,9,6], [2,3,4]], dtype=float)
    b = np.array([29,43,20], dtype=float)
    print(obereDreiecksMatrix(A,b))