import numpy as np

def obereDreiecksMatrix(A,vector):
    # überprüfen dass Matrix quadratisch ist:
    if (len(A) != len(A[0])):
        return
    A = A.astype(np.float64)
    A_triangle = np.copy(A).astype(np.float64)
    b = np.copy(vector).astype(np.float64)
    n = len(A_triangle)
    numberOfRowSwaps = 0

    for i in range(n): 

        # Nullen auf Diagonale eliminieren

        if ((A_triangle[i,i] == 0)):
            rowToSwapWith = -1
            for j in range(i + 1, n):
                if ((A_triangle[j,i] != 0) and (rowToSwapWith == -1)):
                    rowToSwapWith = j

            if(rowToSwapWith == -1):
                print("invalid matrix")
                return
            
            copyA = np.copy(A_triangle)
            A_triangle[i] = copyA[rowToSwapWith]
            A_triangle[rowToSwapWith] = copyA[i]

            copyb = np.copy(b)
            b[i] = copyb[rowToSwapWith]
            b[rowToSwapWith] = copyb[i]

            numberOfRowSwaps += 1

        # Eliminationsschritt

        for j in range(i + 1, n):
            b[j] = b[j] - A_triangle[j,i]/A_triangle[i,i] * b[i] 
            A_triangle[j] = A_triangle[j] - A_triangle[j,i]/A_triangle[i,i] * A_triangle[i]

    # Determinante berechnen

    detA = (-1) ** numberOfRowSwaps
    for i in range(n):
        detA *= A_triangle[i,i]
    
    # auflösen nach x

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i] -= A_triangle[i,j] * x[j]

        x[i] = b[i] / A_triangle[i,i]

    return [A_triangle, detA, x]


# Wird nur ausgeführt wenn explizit dieses Script ausgeführt wird. 
if __name__ == "__main__":

    A = np.array([[1, 5, 6], [7,9,6], [2,3,4]])
    b = np.array([29,43,20], dtype=float)
    print(obereDreiecksMatrix(A,b))