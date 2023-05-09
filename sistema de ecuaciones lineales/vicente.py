from sympy import Abs

def jacobi(MATRIZ_M, MATRIZ_N, LIM, LATITUD):
    matiz_x = [0, 0, 0]
    for i in range(LIM):
        n = len(MATRIZ_M)
        temp_list = []
        for j in range(n):
            temp_list.append(MATRIZ_M[j][0] * matiz_x[0] + MATRIZ_M[j][1] * matiz_x[1] + MATRIZ_M[j][2] * matiz_x[2] + MATRIZ_N[j])
        print(f'Iteracion {i + 1}: {temp_list}')
        error = error_jacobi(matiz_x, temp_list, MATRIZ_M)
        print(f'Error absoluto: {error}')
        if error < LATITUD:
            break
        matiz_x = temp_list

def error_jacobi(matriz_1, matriz_2, MATRIZ_M):
    temp_list = []
    for i in range(len(matriz_1)):
        temp_list.append(matriz_1[i] - matriz_2[i])
    maximo = float(max(temp_list))
    alfa = calcular_alfa(MATRIZ_M)
    error = alfa / (1 - alfa) * maximo
    return Abs(error)

def calcular_alfa(MATRIZ_M):
    tem_list = []
    for j in range(len(MATRIZ_M)):
        tem_list.append(Abs(MATRIZ_M[j][0]) + Abs(MATRIZ_M[j][1]) + Abs(MATRIZ_M[j][2]))
    maximo = float(max(tem_list))
    return maximo

MATRIZ_M=[[0,-1/10,0],[-1/10, 0, -1/10],[0, -1/10, 0]]
MATRIZ_N=[11/10, 12/10, 11/10]
LIM=5
LATITUD= 10**-100
jacobi(MATRIZ_M=MATRIZ_M, MATRIZ_N=MATRIZ_N, LIM=5, LATITUD=LATITUD)