from sympy import symbols, Eq, solve

ax, ay = symbols('ax ay')

m = 2  # kg

# Newton's second law: sum F = m*a, one equation per direction
eq_x = Eq(-4 + 2, m*ax)   # sum Fx = m*ax
eq_y = Eq(3 - 3, m*ay)    # sum Fy = m*ay

print(solve([eq_x, eq_y], (ax, ay)))