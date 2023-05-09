from sympy import symbols, diff, solve, exp

x = symbols('x')
f = x*exp(-x)
df = diff(f, x)
critical_points = solve(df, x)

max_value = max([f.subs(x, cp) for cp in critical_points])
max_point = (critical_points[0], max_value)

print(max_point)