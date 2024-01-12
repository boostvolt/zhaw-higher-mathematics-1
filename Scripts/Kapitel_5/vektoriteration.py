import numpy as np
import numpy.linalg as linalg


def max_eigenwert_anzahl_iterationen(A, v_0, anzahl_iterationen, debug=False):
    A = np.array(A, dtype=np.float64)
    v = np.array(v_0, dtype=np.float64)
    eigenwert = -100
    for i in range(anzahl_iterationen):
        A_v = A @ v
        if debug:
            print("----------------------------")
            print("Iteration: ", i + 1)
            print(
                f"Av = A * v_{i} =\n{A}\n * \n{v.reshape(-1, 1)}\n = \n{A_v.reshape(-1, 1)}\n"
            )
            print()
            print(
                f"v_{i + 1} = Av / ( ||Av||_2 ) = \n{A_v.reshape(-1, 1)}\n / {linalg.norm(A_v, 2)} = \n{A_v / linalg.norm(A_v, 2).reshape(-1, 1)}"
            )
            print()
            print(
                f"λ_{i + 1} = (v_{i})^T * Av_{i} / (v_{i})^T * v_{i} = \n{v.T}\n * \n{A_v.reshape(-1, 1)}\n / (\n{v.T}\n * \n{v.reshape(-1, 1)}) = {(v.T @ A_v) / (v.T @ v)}"
            )
            print()
            print(
                f"λ_{i + 1}: {(v.T @ A_v) / (v.T @ v)} -> v_{i + 1}: {A_v / linalg.norm(A_v, 2)}"
            )

        v_next = A_v / linalg.norm(A_v, 2)  # ord 2 = norm 2
        eigenwert = (v.T @ A_v) / (v.T @ v)
        v = v_next
    return eigenwert, v


def max_eigenwert_toleranz(A, v_0, toleranz, debug=False):
    A = np.array(A, dtype=np.float64)

    v_next = np.array([-100, -100, -100])
    v_previous = np.array(v_0, dtype=np.float64)
    iteration_count = 0

    while np.abs(linalg.norm(v_next - v_previous, ord=2)) > toleranz:
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            v_previous = np.array(v_next)
        A_v = A @ v_previous
        v_next = A_v / linalg.norm(A_v, ord=2)  # ord 2 = norm 2
        eigenwert_näherung = (v_previous.T @ A_v) / (v_previous.T @ v_previous)
        iteration_count = iteration_count + 1
        if debug:
            print("----------------------------")
            print("Iteration: ", iteration_count)
            print(
                f"Av = A * v_{iteration_count} =\n{A}\n * \n{v_previous.reshape(-1, 1)}\n = \n{A_v.reshape(-1, 1)}\n"
            )
            print()
            print(
                f"v_{iteration_count} = Av / ( ||Av||_2 ) = \n{A_v.reshape(-1, 1)}\n / {linalg.norm(A_v, ord=2)} = \n{v_next.reshape(-1, 1)}"
            )
            print()
            print(
                f"λ_{iteration_count} = (v_{iteration_count})^T * Av_{iteration_count} / (v_{iteration_count})^T * v_{iteration_count} = \n{v_previous.T}\n * \n{A_v.reshape(-1, 1)}\n / (\n{v_previous.T}\n * \n{v_previous.reshape(-1, 1)}\n) = {eigenwert_näherung}"
            )
            print()
            print(
                f"λ_{iteration_count}: {eigenwert_näherung} -> v_{iteration_count}: {v_next}"
            )

    return eigenwert_näherung, v_next


A = np.array([[1, 1, 0], [3, -1, 2], [2, -1, 3]])
startvektor = np.array([1, 0, 0])

# A = np.array([[0, -2], [-2, 3]])
# startvektor = np.array([-2, 3])

toleranz = 10**-4

# Mit Anzahl Iterationen
eigenwert, eigenvektor = max_eigenwert_anzahl_iterationen(A, startvektor, 9, True)

# Mit toleranz
# eigenwert, eigenvektor = max_eigenwert_toleranz(A, startvektor, toleranz, True)
