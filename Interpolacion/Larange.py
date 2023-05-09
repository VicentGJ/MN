import sympy
from sympy.functions import factorial, Abs

# numlist=[[x],[y]]
num_list=[[-1,0,1],[0.37,1,2.72]]
# para hacer un polinomio de grado n necesito n+1 nodos

def inter_larange(x, num_list):
    result=0
    for i in range(len(num_list[0])):
        L=1
        for j in range(len(num_list[0])):
            if i!=j:
                L*=(x-num_list[0][j])/(num_list[0][i]-num_list[0][j])
                print(f'gshs: {num_list[0][i]-num_list[0][j]}')
        print(f'L{i}: {L}')
        result+=L*num_list[1][i]
    print(f'Aproximacion: {result}')
    return result

# siempre se da el error absoluto, o sea, el valor es modular
def error_larange(x, M):
    result= M/factorial(len(num_list[0])+1)
    for i in range(len(num_list[0])):
        Xi=x-num_list[0][i]
        print(f'X{i}: {Xi}')
        result*=Xi
    result= Abs(result)
    print(f'Error: {result}')

inter_larange(0.5, num_list)
error_larange(0.5, 7.39)