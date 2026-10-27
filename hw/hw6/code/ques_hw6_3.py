from sympy import symbols, Eq, solve, simplify, N

# Symbols
f, a, n = symbols('f_s a n', positive=True)
m, g, v_i, v_f, t = symbols('m g v_i v_f t', positive=True)

# Equations from the FBD and the motion
eqs = [
    Eq(v_f, v_i + a*t),   # kinematics (constant acceleration)
    Eq(f, m*a),           # sum Fx = ma, friction is the only horizontal force
    Eq(n - m*g, 0),       # sum Fy = 0
]

sol = solve(eqs, (f, a, n), dict=True)[0]

print("a   =", simplify(sol[a]))   # symbolic result
print("f_s =", simplify(sol[f]))   # symbolic result

# Plug in the numbers last
vals = {m: 55, g: 9.8, v_i: 0, v_f: 2.0, t: 0.25}

a_val = N(sol[a].subs(vals), 4)
f_val = N(sol[f].subs(vals), 4)
n_val = N(sol[n].subs(vals), 4)

print("a   =", a_val, "m/s^2")
print("f_s =", f_val, "N")
print("n   =", n_val, "N")

# Extra check: smallest coefficient of static friction that makes this possible
print("mu_s needed >=", N(f_val/n_val, 3))