from sympy import symbols, solve, lambdify, exp, Matrix
from pprint import pprint

def bisection(f, a, b, tol):
    d = 0.1 * tol
    L = b - a
    result = []
    while L >= tol:
        x1 = (a + b) / 2 - (d / 2)
        x2 = (a + b) / 2 + (d / 2)
        y1 = f(x1)
        y2 = f(x2)
        result.append({'a': a, 'b': b, 'L': L, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
        if y1 < y2:
            a = x1
        else:
            b = x2
        L = b - a
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

# Example function with constraints using sympy
x = symbols('x')
f = x*exp(-x)
f = lambdify(x, f)

# Find maximum point of function f within interval [0, 10] with tolerance of 0.1
result = bisection(f, 0.3, 2.1, 0.1)
pprint(result)

a = result[len(result)-1]['a']
b = result[len(result)-1]['b']
fa = f(a)
fb = f(b)
x3 = (result[len(result)-1]['a'] + result[len(result)-1]['b'])/2
y3 = f(x3)
print(a)
print(b)
print(x3)
pprint(quad_interpolation(a, b, x3, fa, fb, y3))