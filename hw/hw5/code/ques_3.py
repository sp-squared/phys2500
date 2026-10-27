from sympy import symbols, Eq, solve, cos, sin, rad, N

P = symbols('P', positive=True)   # each player's pull

f = 1000          # N, friction
half = rad(10)    # each rope is 10 degrees from the direction of motion

# Force equations from the FBD (constant velocity, so a = 0)
eq_x = Eq(2*P*cos(half) - f, 0)          # sum Fx = 0
eq_y = Eq(P*sin(half) - P*sin(half), 0)  # sum Fy = 0 (trivially true)

P_sol = solve(eq_x, P)[0]

print(P_sol)         # exact
print(N(P_sol, 4))   # decimal