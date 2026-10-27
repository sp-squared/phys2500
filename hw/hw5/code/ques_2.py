from sympy import symbols, Eq, solve, cos, sin, rad, N

T1, T2 = symbols('T1 T2', positive=True)

F = 100          # N, the known rope
ang = rad(30)    # SymPy trig uses radians, so convert

# Force equations from the FBD (ring in equilibrium)
eq_x = Eq(-T1 + F*cos(ang), 0)   # sum Fx = 0
eq_y = Eq( T2 - F*sin(ang), 0)   # sum Fy = 0

sol = solve([eq_x, eq_y], (T1, T2))

print(sol)                   # exact values
print(N(sol[T1], 4))         # T1 as a decimal
print(N(sol[T2], 4))         # T2 as a decimal