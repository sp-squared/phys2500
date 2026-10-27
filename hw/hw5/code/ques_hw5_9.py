from sympy import symbols, Eq, solve, sin, cos, rad, N

fs, n = symbols('f_s n')

m = 4000          # kg
g = 9.8           # m/s^2
th = rad(15)      # slope angle, in radians
mu_s = 0.90

eq_x = Eq(fs - m*g*sin(th), 0)   # sum Fx = 0 (along the slope)
eq_y = Eq(n - m*g*cos(th), 0)    # sum Fy = 0 (perpendicular to the slope)

sol = solve([eq_x, eq_y], (fs, n))
f_max = mu_s*sol[n]              # largest static friction possible

print(N(sol[n], 5))              # normal force
print(N(sol[fs], 5))             # friction actually needed
print(N(f_max, 5))               # maximum static friction
print(N(sol[fs]) <= N(f_max))    # True means the truck stays put