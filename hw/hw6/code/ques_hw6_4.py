from sympy import symbols, Eq, solve, simplify, sqrt, N

# Unknowns: F = size of the head's push on the ball, a = ball's x-acceleration
F, a = symbols('F a')
m, v_i, v_f, t = symbols('m v_i v_f t', positive=True)

# Equations from the FBD and the motion (+x is the ball's direction of travel)
eqs = [
    Eq(v_f, v_i + a*t),   # kinematics, constant acceleration
    Eq(-F, m*a),          # sum Fx = ma, the head's push points backward
]

sol = solve(eqs, (F, a), dict=True)[0]

print(simplify(sol[a]))   # symbolic acceleration
print(simplify(sol[F]))   # symbolic force

# Plug in the numbers last (SI units)
vals = {m: 0.140, v_i: 30, v_f: 0, t: 0.0015}

a_val = N(sol[a].subs(vals), 4)
F_val = N(sol[F].subs(vals), 4)

print("a =", a_val, "m/s^2")
print("(a) F =", F_val, "N")

# Part (b): Newton's third law, equal size, opposite direction
print("(b) force on head =", F_val, "N (forward)")

# Part (c): compare with the bone limits
limits = {"forehead": 6000, "cheekbone": 1300}
for name, limit in limits.items():
    ratio = N(F_val/limit, 3)
    verdict = "safe" if F_val < limit else "fracture risk"
    print("(c)", name + ":", "ratio", ratio, "->", verdict)

# Extra: does including the weight change the force? (it acts down, F acts backward)
w = 0.140*9.8
print("with weight included:", N(sqrt(F_val**2 + w**2), 10), "N")