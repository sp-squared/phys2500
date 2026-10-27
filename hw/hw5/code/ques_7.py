from sympy import symbols, Eq, solve, N

n, f, mu = symbols('n f mu', positive=True)

m = 300           # kg
g = 9.8           # m/s^2
F_clyde = 385     # N, push from behind
F_bonnie = 350    # N, pull on the rope

eq_y = Eq(n - m*g, 0)                  # sum Fy = 0
eq_x = Eq(F_clyde + F_bonnie - f, 0)   # sum Fx = 0 (constant speed)
eq_f = Eq(f, mu*n)                     # kinetic friction model

sol = solve([eq_y, eq_x, eq_f], (n, f, mu), dict=True)[0]

print(N(sol[n], 4))    # normal force
print(N(sol[f], 4))    # friction force
print(N(sol[mu], 4))   # coefficient of kinetic friction