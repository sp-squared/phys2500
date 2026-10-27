from sympy import symbols, Eq, solve, N

a, f = symbols('a f', positive=True)

m = 55      # kg
v0 = 0      # m/s, starts from rest
v = 6.0     # m/s, final speed
t = 4.5     # s
T = 120     # N, tension

# Step 1: kinematics gives the acceleration
eq_kin = Eq(v, v0 + a*t)

# Step 2: Newton's second law along x (forward positive)
eq_x = Eq(T - f, m*a)

sol = solve([eq_kin, eq_x], (a, f))

print(N(sol[a], 4))   # acceleration
print(N(sol[f], 4))   # friction