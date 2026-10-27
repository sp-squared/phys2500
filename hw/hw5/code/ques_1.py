from sympy import symbols, Eq, solve, sqrt, atan, deg, N

T3x, T3y = symbols('T3x T3y')

sol = solve([Eq(-50 + T3x, 0),
             Eq(80 + T3y, 0)], (T3x, T3y))

mag = sqrt(sol[T3x]**2 + sol[T3y]**2)
angle = deg(atan(abs(sol[T3y]) / abs(sol[T3x])))

print(sol)            # {T3x: 50, T3y: -80}
print(N(mag, 4))      # 94.34
print(N(angle, 4))    # 57.99