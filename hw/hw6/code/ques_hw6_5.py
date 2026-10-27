from sympy import symbols, Eq, solve, simplify, N

# Unknowns: shared acceleration, and the contact forces between neighbors
a, F12, F23 = symbols('a F12 F23', positive=True)
m1, m2, m3, F_app = symbols('m1 m2 m3 F_app', positive=True)

# One equation per block (forward is positive)
eqs = [
    Eq(F_app - F12, m1*a),   # block 1: applied push forward, block 2 pushes back
    Eq(F12 - F23, m2*a),     # block 2: block 1 pushes forward, block 3 pushes back
    Eq(F23, m3*a),           # block 3: only block 2 pushes it forward
]

sol = solve(eqs, (a, F12, F23), dict=True)[0]

print("a   =", simplify(sol[a]))
print("F23 =", simplify(sol[F23]))   # force of 2 on 3 (part a)
print("F12 =", simplify(sol[F12]))   # force between 1 and 2 (part b)

# Plug in the numbers last
vals = {m1: 1, m2: 2, m3: 3, F_app: 12}

print("a   =", N(sol[a].subs(vals), 4), "m/s^2")
print("(a) 2 on 3 =", N(sol[F23].subs(vals), 4), "N")
print("(b) 2 on 1 =", N(sol[F12].subs(vals), 4), "N")

# Check: the internal pushes cancel, so the whole system obeys F = (m1+m2+m3)a
a_val = sol[a].subs(vals)
print("whole-system check:", N(12 - (1 + 2 + 3)*a_val, 6))   # should be 0