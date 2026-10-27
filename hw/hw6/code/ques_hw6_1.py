from sympy import symbols, Eq, solve, cos, sin, rad, N

TB, Tw, TA, mA, n = symbols('T_B T_w T_A m_A n', positive=True)

mB = 20          # kg
g = 9.8          # m/s^2
mu_s = 0.60
th = rad(45)     # angle of the wall rope above horizontal

eqs = [
    Eq(-TB + Tw*cos(th), 0),   # knot, sum Fx = 0
    Eq(Tw*sin(th) - TA, 0),    # knot, sum Fy = 0
    Eq(TA - mA*g, 0),          # block A at rest
    Eq(n - mB*g, 0),           # block B, vertical
    Eq(TB, mu_s*n),            # block B about to slip
]

sol = solve(eqs, (TB, Tw, TA, mA, n), dict=True)[0]

for name, val in sol.items():
    print(name, N(val, 4))