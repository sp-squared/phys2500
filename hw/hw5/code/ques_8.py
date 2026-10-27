from sympy import symbols, Eq, solve, N

f_s = symbols('f_s')

m = 30          # kg
g = 9.8         # m/s^2
mu_s = 0.80
F = 200         # N, Bob's pull

n = m*g                       # from sum Fy = 0
f_max = mu_s*n                # largest static friction possible

eq_x = Eq(F - f_s, 0)         # sum Fx = 0 (cabinet doesn't move)
f_needed = solve(eq_x, f_s)[0]

print(N(n, 4))                # normal force
print(N(f_max, 4))            # maximum static friction
print(f_needed)               # friction actually acting
print(f_needed <= f_max)      # True means it really stays at rest