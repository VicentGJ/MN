from sympy import symbols, solve, lambdify, exp, Matrix, sqrt, sin
from pprint import pprint
from math import pi

def bisection(f, a, b, tol, max_iter=0):
    d = 0.1 * tol
    L = b - a
    result = []
    while L >= tol:
        x1 = (a + b) / 2 - (d / 2)
        x2 = (a + b) / 2 + (d / 2)
        y1 = f(x1)
        y2 = f(x2)
        result.append({'a': a, 'b': b, 'L': L, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
        if y1 < y2: # Esta comparción cambia dependiendo si es mínimo o máximo
            a = x1
        else:
            b = x2
        L = b - a
        if len(result) > max_iter + 1 and max_iter != 0:
            break
    result.append({'a': a, 'b': b, 'L': L, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
    return result

def golden_section(f, a, b, tol):
    Factor = 0.382
    L = b - a
    x1 = a + Factor * L
    x2 = b - Factor * L
    y1 = f(x1)
    y2 = f(x2)
    result = []
    while L >= tol:
        result.append({'a': a, 'b': b, 'L': L, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
        if y1 > y2: # Esta comparción cambia dependiendo si es mínimo o máximo
            a = x1
            x1 = x2
            y1 = y2
            L = b - a
            x2 = b - Factor * L
            y2 = f(x2)
        else:
            b = x2
            x2 = x1
            y2 = y1
            L = b - a
            x1 = a + Factor * L
            y1 = f(x1)
    result.append({'a': a, 'b': b, 'L': L, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
    return result

def quadratic_interpolation(x1, x2, x3, y1, y2, y3):
    x12 = (x1+x2)/2
    x23 = (x2+x3)/2
    f12 = (y2-y1)/(x2-x1)
    f23 = (y3-y2)/(x3-x2)
    aprox = (x23*f12-x12*f23)/(f12-f23)
    return aprox

def quad_interpolation(x1, x2, x3, y1, y2, y3):
    x = symbols('x')
    A = Matrix([[x1**2,x1,1],[x2**2,x2,1],[x3**2,x3,1]])
    b=Matrix([y1,y2,y3])
    a,b,c=A.inv()*b

    # Calculate vertex of quadratic polynomial
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    vertex = (h, k)

    return vertex

# Example function using sympy
x = symbols('x')
f = x * sin(pi/2 + x/2)
f = lambdify(x, f)

# Find maximum point of function f within interval with a given tolerance
result = bisection(f, 0, pi, 0.0001, max_iter=2)
pprint(result)

a = result[len(result)-1]['a'] # Valor de a en la última iteración
b = result[len(result)-1]['b'] # Valor de b en la última iteración
fa = f(a)
fb = f(b)
x3 = (a + b)/2
y3 = f(x3)
pprint(quadratic_interpolation(a, b, x3, fa, fb, y3))