from sympy import symbols, lambdify, exp
from pprint import pprint

def rk2(f, g, x0, y0, z0, h, n):
    results = []
    results.append({'x': x0,
                'y': y0,
                'z': z0,
                'k1': '-',
                'k2': '-',
                'l1': '-',
                'l2': '-'})
    i = 0
    while i < n:
        i += 1
        k1 = h * f(x0, y0, z0)
        l1 = h * g(x0, y0, z0)
        x0 += h
        k2 = h * f(x0, y0 + k1, z0 + l1)
        l2 = h * g(x0, y0 + k1, z0 + l1)
        y0 = y0 + ((k1+k2)/2)
        z0 = z0 + ((l1+l2)/2)
        results.append({'x': x0,
                'y': y0,
                'z': z0,
                'k1': k1,
                'k2': k2,
                'l1': l1,
                'l2': l2})
    return results
    
x = symbols('x')
y = symbols('y')
z = symbols('z')

f = 2*x + x**3 - z
g = 4*x**2 - y
f = lambdify([x, y, z], f)
g = lambdify([x, y, z], g)
x0 = 0
xn = 2
y0=1
z0=1
h = 0.5
n = (xn - x0)/h

result = rk2(f, g, x0, y0, z0, h, n)
pprint(result)